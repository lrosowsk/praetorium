"""Simulated distribution substation that speaks Modbus TCP.

Three feeders, each behind a breaker (coils 0-2), a voltage regulator
(holding registers: tap position, voltage setpoint) and live measurements
(input registers: feeder loads, bus voltage, frequency).

This stands in for the RTU/PLC a real utility would have. Nothing here is
connected to real equipment.
"""

import argparse
import logging
import random
import threading
import time

from pymodbus.datastore import (
    ModbusSequentialDataBlock,
    ModbusServerContext,
    ModbusSlaveContext,
)
from pymodbus.server import StartTcpServer

# Register layout (shared with gateway.py via points.json)
COILS, HOLDING, INPUT = 1, 3, 4
TAP_OFFSET = 16  # tap -16..+16 stored as 0..32
BASE_LOADS = [3200, 2700, 4100]  # kW per feeder


def physics(store: ModbusSlaveContext, stop: threading.Event) -> None:
    loads = list(BASE_LOADS)
    while not stop.is_set():
        breakers = store.getValues(COILS, 0, 3)
        tap_raw, setpoint = store.getValues(HOLDING, 0, 2)
        tap = tap_raw - TAP_OFFSET
        live = []
        for i, closed in enumerate(breakers):
            loads[i] = max(500, min(6000, loads[i] + random.randint(-80, 80)))
            live.append(loads[i] if closed else 0)
        total_mw = sum(live) / 1000
        # Bus voltage (x10 V): setpoint, plus 0.625% per tap step, minus load droop
        volts = setpoint / 10 * (1 + tap * 0.00625) - total_mw * 0.35
        freq = 6000 + random.randint(-2, 2)  # Hz x100
        store.setValues(INPUT, 0, live + [max(0, int(volts * 10)), freq])
        time.sleep(1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=5020)
    args = parser.parse_args()
    logging.basicConfig(level=logging.WARNING)

    store = ModbusSlaveContext(
        co=ModbusSequentialDataBlock(0, [1, 1, 1] + [0] * 17),
        hr=ModbusSequentialDataBlock(0, [TAP_OFFSET, 1200] + [0] * 18),
        ir=ModbusSequentialDataBlock(0, [0] * 20),
        di=ModbusSequentialDataBlock(0, [0] * 20),
        zero_mode=True,  # register N on the wire is index N in the block
    )
    context = ModbusServerContext(slaves=store, single=True)
    stop = threading.Event()
    threading.Thread(target=physics, args=(store, stop), daemon=True).start()
    print(f"[substation] Modbus TCP listening on 127.0.0.1:{args.port}", flush=True)
    StartTcpServer(context=context, address=("127.0.0.1", args.port))


if __name__ == "__main__":
    main()
