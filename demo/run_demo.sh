#!/usr/bin/env bash
# Start the simulated substation and the Preceptor gate, then run the agent scenario.
# Open http://127.0.0.1:8080 to watch, and approve the copilot's request when it appears.
set -euo pipefail
cd "$(dirname "$0")"

python3 substation.py & SUB=$!
sleep 1
python3 gateway.py & GATE=$!
trap 'kill $SUB $GATE 2>/dev/null' EXIT
sleep 1

echo "Dashboard: http://127.0.0.1:8080"
python3 agents.py "$@"
echo "Press Ctrl+C to stop."
wait
