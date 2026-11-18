"""The Praetorium gate (demo).

AI agents never talk Modbus directly. They call this gateway's tool API, and
every request is:

  1. identified   - is this a registered agent, and who owns it?
  2. checked      - is the action inside the agent's policy?
  3. held         - risky writes wait for a human ("hold point")
  4. watched      - machine-speed scanning gets the agent quarantined
  5. logged       - a hash-chained, tamper-evident audit trail

It also serves the operator dashboard and a compliance evidence report.
"""

import argparse
import hashlib
import json
import threading
import time
import uuid
from collections import defaultdict, deque
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from pymodbus.client import ModbusTcpClient

HERE = Path(__file__).parent
POINTS = json.loads((HERE / "points.json").read_text())
POLICY = json.loads((HERE / "policy.json").read_text())


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")[:-4] + "Z"


class OT:
    """Thin, locked Modbus client for the simulated substation."""

    def __init__(self, port: int):
        self.client = ModbusTcpClient("127.0.0.1", port=port)
        self.lock = threading.Lock()

    def _ensure(self):
        if not self.client.connected:
            self.client.connect()

    def read(self, name: str):
        p = POINTS[name]
        with self.lock:
            for attempt in range(2):
                self._ensure()
                if p["type"] == "coil":
                    rr = self.client.read_coils(p["address"], 1, slave=1)
                elif p["type"] == "holding":
                    rr = self.client.read_holding_registers(p["address"], 1, slave=1)
                else:
                    rr = self.client.read_input_registers(p["address"], 1, slave=1)
                if not rr.isError():
                    break
                self.client.close()  # reconnect once on a transport hiccup
            else:
                raise IOError(f"Modbus read failed for {name}: {rr}")
            if p["type"] == "coil":
                return bool(rr.bits[0])
            return rr.registers[0] - p.get("offset", 0)

    def write(self, name: str, value):
        p = POINTS[name]
        with self.lock:
            self._ensure()
            if p["type"] == "coil":
                self.client.write_coil(p["address"], bool(value), slave=1)
            else:
                self.client.write_register(p["address"], int(value) + p.get("offset", 0), slave=1)


class Gate:
    def __init__(self, ot: OT, log_path: Path):
        self.ot = ot
        self.lock = threading.RLock()
        self.log_path = log_path
        self.log_path.write_text("")
        self.audit: list[dict] = []
        self.prev_hash = "0" * 64
        self.pending: dict[str, dict] = {}
        self.resolved: dict[str, dict] = {}
        self.alerts: list[dict] = []
        self.quarantined: set[str] = set()
        self.recent: dict[str, deque] = defaultdict(deque)
        self.stats: dict[str, dict] = defaultdict(lambda: {"allowed": 0, "held": 0, "denied": 0, "last_seen": None})
        self.unregistered: set[str] = set()

    # --- audit -----------------------------------------------------------
    def log(self, **entry) -> dict:
        with self.lock:
            entry = {"ts": now(), **entry, "prev": self.prev_hash}
            digest = hashlib.sha256(json.dumps(entry, sort_keys=True).encode()).hexdigest()
            entry["hash"] = digest
            self.prev_hash = digest
            self.audit.append(entry)
            with self.log_path.open("a") as f:
                f.write(json.dumps(entry) + "\n")
            return entry

    def verify_chain(self) -> bool:
        prev = "0" * 64
        for e in self.audit:
            body = {k: v for k, v in e.items() if k != "hash"}
            if body["prev"] != prev:
                return False
            if hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest() != e["hash"]:
                return False
            prev = e["hash"]
        return True

    def alert(self, severity: str, agent: str, message: str):
        self.alerts.append({"ts": now(), "severity": severity, "agent": agent, "message": message})

    # --- policy ----------------------------------------------------------
    def _decide(self, agent: str, action: str, point: str, value, kind: str, reason: str, **extra):
        self.stats[agent][kind] += 1
        entry = self.log(agent=agent, action=action, point=point, value=value, decision=kind, reason=reason)
        return {"decision": kind, "reason": reason, "audit_id": entry["hash"][:12], **extra}

    def _scanning(self, agent: str, point: str) -> bool:
        d = POLICY["detection"]
        q = self.recent[agent]
        t = time.time()
        q.append((t, point))
        while q and t - q[0][0] > d["window_seconds"]:
            q.popleft()
        distinct = len({p for _, p in q})
        return len(q) > d["max_requests"] or distinct > d["max_distinct_points"]

    def request(self, agent: str, action: str, point: str, value=None) -> dict:
        with self.lock:
            spec = POLICY["agents"].get(agent)
            if agent in self.stats or spec:
                self.stats[agent]["last_seen"] = now()

            if spec is None:
                if agent not in self.unregistered:
                    self.unregistered.add(agent)
                    self.alert("high", agent, "Unregistered AI agent tried to reach OT. Blocked and added to inventory for review.")
                self.stats[agent]["last_seen"] = now()
                return self._decide(agent, action, point, value, "denied", "Unregistered AI agent")

            if agent in self.quarantined:
                return self._decide(agent, action, point, value, "denied", "Agent quarantined after anomaly")

            if self._scanning(agent, point):
                self.quarantined.add(agent)
                d = POLICY["detection"]
                self.alert("critical", agent,
                           f"Machine-speed reconnaissance: more than {d['max_distinct_points']} points or "
                           f"{d['max_requests']} requests in {d['window_seconds']}s. Agent quarantined.")
                return self._decide(agent, action, point, value, "denied", "Machine-speed reconnaissance detected; agent quarantined")

            if point not in POINTS:
                return self._decide(agent, action, point, value, "denied", "Unknown point")

            cls = POINTS[point]["class"]
            if action == "read":
                if "*" in spec["read"] or point in spec["read"]:
                    v = self.ot.read(point)
                    return self._decide(agent, action, point, None, "allowed", "Inside agent's read scope", result=v)
                return self._decide(agent, action, point, None, "denied", "Outside agent's read scope")

            if action == "write":
                if cls == "protection":
                    self.alert("high", agent, f"Attempted write to {POINTS[point]['label']}. Protection equipment is never reachable by AI.")
                    return self._decide(agent, action, point, value, "denied", "Protection equipment: never reachable by AI")
                if point not in spec["write"]:
                    return self._decide(agent, action, point, value, "denied", "Agent not permitted to write this point")
                if POLICY["class_rules"].get(cls) == "approve":
                    hold_id = uuid.uuid4().hex[:8]
                    current = self.ot.read(point)
                    self.pending[hold_id] = {
                        "id": hold_id, "agent": agent, "point": point, "label": POINTS[point]["label"],
                        "current": current, "value": value, "requested_at": now(),
                        "owner": spec["owner"],
                    }
                    return self._decide(agent, action, point, value, "held", "Control action: held for human approval", hold_id=hold_id)
                return self._decide(agent, action, point, value, "denied", "No write rule")

            return self._decide(agent, action, point, value, "denied", "Unknown action")

    def resolve(self, hold_id: str, approve: bool, approver: str) -> dict:
        with self.lock:
            hold = self.pending.pop(hold_id, None)
            if not hold:
                return {"error": "no such hold"}
            if approve:
                self.ot.write(hold["point"], hold["value"])
                outcome = "approved"
            else:
                outcome = "rejected"
            self.log(agent=hold["agent"], action="write", point=hold["point"], value=hold["value"],
                     decision=outcome, reason=f"Hold point resolved by {approver}", approver=approver, hold_id=hold_id)
            self.resolved[hold_id] = {**hold, "outcome": outcome, "approver": approver, "resolved_at": now()}
            return {"outcome": outcome}

    def release(self, agent: str, approver: str) -> dict:
        with self.lock:
            self.quarantined.discard(agent)
            self.recent[agent].clear()
            self.log(agent=agent, action="release", point=None, value=None, decision="released",
                     reason=f"Quarantine lifted by {approver}", approver=approver)
            return {"released": agent}

    # --- views -----------------------------------------------------------
    def grid(self) -> dict:
        try:
            return {name: self.ot.read(name) for name in POINTS}
        except Exception as exc:  # substation not up yet
            return {"error": str(exc)}

    def state(self) -> dict:
        with self.lock:
            agents = []
            for name, spec in POLICY["agents"].items():
                agents.append({"name": name, **{k: spec[k] for k in ("description", "owner", "source")},
                               "registered": True, "status": "quarantined" if name in self.quarantined else "active",
                               **self.stats[name]})
            for name in sorted(self.unregistered):
                agents.append({"name": name, "description": "Unknown AI agent", "owner": "Unknown",
                               "source": "Unknown", "registered": False, "status": "blocked", **self.stats[name]})
            return {
                "grid": self.grid(),
                "agents": agents,
                "pending": list(self.pending.values()),
                "alerts": list(reversed(self.alerts))[:12],
                "audit": list(reversed(self.audit))[:18],
                "audit_count": len(self.audit),
                "chain_ok": self.verify_chain(),
            }

    def report(self) -> str:
        with self.lock:
            totals = defaultdict(int)
            for e in self.audit:
                totals[e["decision"]] += 1
            lines = [
                "# Praetorium: AI access evidence report",
                "",
                f"Generated {now()} (demo environment, simulated substation)",
                "",
                "## Summary",
                "",
                f"- Audit entries: {len(self.audit)}; hash chain intact: **{'yes' if self.verify_chain() else 'NO'}**",
                f"- Decisions: {dict(totals)}",
                f"- Open hold points: {len(self.pending)}; alerts raised: {len(self.alerts)}",
                "",
                "## AI agent inventory",
                "",
                "| Agent | Owner | Source | Status | Allowed | Held | Denied |",
                "|---|---|---|---|---|---|---|",
            ]
            for a in self.state()["agents"]:
                lines.append(f"| {a['name']} | {a['owner']} | {a['source']} | {a['status']} | {a['allowed']} | {a['held']} | {a['denied']} |")
            lines += ["", "## Control actions and approvals", "",
                      "| Requested | Agent | Point | From | To | Outcome | Approver |", "|---|---|---|---|---|---|---|"]
            for h in self.resolved.values():
                lines.append(f"| {h['requested_at']} | {h['agent']} | {h['label']} | {h['current']} | {h['value']} | {h['outcome']} | {h['approver']} |")
            for h in self.pending.values():
                lines.append(f"| {h['requested_at']} | {h['agent']} | {h['label']} | {h['current']} | {h['value']} | pending | - |")
            lines += ["", "## Alerts", ""]
            lines += [f"- {a['ts']} [{a['severity']}] {a['agent']}: {a['message']}" for a in self.alerts] or ["- None"]
            lines += ["", "## How this supports compliance", "",
                      "- Inventory of every AI agent that touched operational systems, including unregistered ones.",
                      "- A record of every AI request inside the control network, supporting internal network security monitoring (NERC CIP-015).",
                      "- Human approval recorded for every AI-initiated control action.",
                      "- Tamper-evident log: each entry carries the hash of the one before it.",
                      "", "_Demo output. Not a compliance determination._"]
            return "\n".join(lines) + "\n"


def make_handler(gate: Gate):
    dashboard = (HERE / "dashboard.html").read_bytes()

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def _send(self, code, body, ctype="application/json", extra=None):
            data = body if isinstance(body, bytes) else (json.dumps(body) if ctype == "application/json" else body).encode()
            self.send_response(code)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(data)))
            for k, v in (extra or {}).items():
                self.send_header(k, v)
            self.end_headers()
            self.wfile.write(data)

        def _body(self):
            n = int(self.headers.get("Content-Length") or 0)
            return json.loads(self.rfile.read(n) or b"{}")

        def do_GET(self):
            if self.path in ("/", "/index.html"):
                return self._send(200, dashboard, "text/html; charset=utf-8")
            if self.path == "/api/state":
                return self._send(200, gate.state())
            if self.path == "/api/report":
                return self._send(200, gate.report(), "text/markdown; charset=utf-8",
                                  {"Content-Disposition": 'attachment; filename="praetorium-evidence-report.md"'})
            if self.path.startswith("/api/hold/"):
                hid = self.path.rsplit("/", 1)[-1]
                if hid in gate.pending:
                    return self._send(200, {"status": "pending"})
                if hid in gate.resolved:
                    return self._send(200, {"status": gate.resolved[hid]["outcome"]})
                return self._send(404, {"error": "unknown hold"})
            return self._send(404, {"error": "not found"})

        def do_POST(self):
            try:
                self._post()
            except Exception as exc:  # keep the gate up and tell the caller
                self._send(500, {"decision": "error", "reason": str(exc)})

        def _post(self):
            body = self._body()
            if self.path == "/api/tool":
                result = gate.request(body.get("agent", "unknown"), body.get("action"), body.get("point"), body.get("value"))
                return self._send(200, result)
            if self.path.startswith("/api/approve/") or self.path.startswith("/api/reject/"):
                hid = self.path.rsplit("/", 1)[-1]
                approver = body.get("approver", "Control room operator")
                return self._send(200, gate.resolve(hid, self.path.startswith("/api/approve/"), approver))
            if self.path.startswith("/api/release/"):
                return self._send(200, gate.release(self.path.rsplit("/", 1)[-1], body.get("approver", "Security analyst")))
            return self._send(404, {"error": "not found"})

    return Handler


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8080)
    parser.add_argument("--modbus-port", type=int, default=5020)
    args = parser.parse_args()
    gate = Gate(OT(args.modbus_port), HERE / "audit.jsonl")
    server = ThreadingHTTPServer(("127.0.0.1", args.port), make_handler(gate))
    print(f"[gateway] Praetorium gate and dashboard on http://127.0.0.1:{args.port}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
