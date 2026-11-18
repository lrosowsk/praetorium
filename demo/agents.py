"""Scripted AI agents for the demo.

  forecast-model   reads loads every few seconds            -> allowed
  ems-copilot      asks to raise the regulator tap           -> held for a human
  shadow-agent     an AI tool nobody registered              -> blocked, added to inventory
  eng-assistant-7  tries to open a breaker, then scans fast  -> denied, then quarantined

Run after substation.py and gateway.py are up. Approve or reject the
copilot's request on the dashboard, or pass --approve-after N to have the
script approve it automatically (handy for recordings and tests).
"""

import argparse
import json
import threading
import time
import urllib.request

GATE = "http://127.0.0.1:8080"


def call(path, payload=None):
    req = urllib.request.Request(
        GATE + path,
        data=json.dumps(payload or {}).encode() if payload is not None else None,
        headers={"Content-Type": "application/json"},
        method="POST" if payload is not None else "GET",
    )
    with urllib.request.urlopen(req, timeout=10) as r:
        return json.loads(r.read())


def tool(agent, action, point, value=None):
    return call("/api/tool", {"agent": agent, "action": action, "point": point, "value": value})


def say(agent, msg):
    print(f"{time.strftime('%H:%M:%S')}  {agent:<16} {msg}", flush=True)


def forecaster(stop):
    while not stop.is_set():
        vals = [tool("forecast-model", "read", p).get("result") for p in ("feeder_1_load", "feeder_2_load", "feeder_3_load")]
        say("forecast-model", f"read feeder loads {vals} kW -> allowed")
        stop.wait(3)


def copilot(approve_after):
    time.sleep(5)
    v = tool("ems-copilot", "read", "bus_voltage")
    tap = tool("ems-copilot", "read", "regulator_tap").get("result", 0)
    say("ems-copilot", f"bus voltage {v.get('result', 0) / 10:.1f} V looks low; requesting regulator tap {tap:+d} -> {tap + 2:+d}")
    r = tool("ems-copilot", "write", "regulator_tap", tap + 2)
    say("ems-copilot", f"-> {r['decision'].upper()}: {r['reason']}")
    if r["decision"] != "held":
        return
    hold = r["hold_id"]
    if approve_after is not None:
        time.sleep(approve_after)
        call(f"/api/approve/{hold}", {"approver": "Control room operator (scripted)"})
    for _ in range(300):
        status = call(f"/api/hold/{hold}")["status"]
        if status != "pending":
            say("ems-copilot", f"hold point resolved: {status.upper()}")
            return
        time.sleep(1)
    say("ems-copilot", "no decision after 5 minutes; request still pending")


def shadow():
    time.sleep(9)
    r = tool("shadow-agent", "read", "bus_voltage")
    say("shadow-agent", f"-> {r['decision'].upper()}: {r['reason']}")


def rogue():
    time.sleep(13)
    r = tool("eng-assistant-7", "read", "feeder_2_load")
    say("eng-assistant-7", f"read feeder 2 load -> {r['decision']}")
    time.sleep(2)
    r = tool("eng-assistant-7", "write", "feeder_2_breaker", False)
    say("eng-assistant-7", f"tries to OPEN feeder 2 breaker -> {r['decision'].upper()}: {r['reason']}")
    time.sleep(2)
    say("eng-assistant-7", "starts scanning every register at machine speed...")
    targets = list(json.load(open(__file__.replace("agents.py", "points.json")))) + [f"hr_{i}" for i in range(10, 30)]
    for p in targets:
        r = tool("eng-assistant-7", "read", p)
        if "quarantined" in r["reason"]:
            say("eng-assistant-7", f"-> DENIED: {r['reason']}")
            break
    r = tool("eng-assistant-7", "write", "feeder_2_breaker", False)
    say("eng-assistant-7", f"tries the breaker again -> {r['decision'].upper()}: {r['reason']}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--approve-after", type=float, default=None, help="auto-approve the copilot's hold after N seconds")
    parser.add_argument("--duration", type=float, default=45)
    args = parser.parse_args()
    stop = threading.Event()
    threads = [
        threading.Thread(target=forecaster, args=(stop,), daemon=True),
        threading.Thread(target=copilot, args=(args.approve_after,), daemon=True),
        threading.Thread(target=shadow, daemon=True),
        threading.Thread(target=rogue, daemon=True),
    ]
    for t in threads:
        t.start()
    time.sleep(args.duration)
    stop.set()
    print("scenario finished; the dashboard stays live", flush=True)


if __name__ == "__main__":
    main()
