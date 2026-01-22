# Runbook

## How to run (local)
Placeholder. The Whale Watcher script will be added in Phase 1.

## Evidence
Placeholder. Logs and SQLite rows will be stored in docs/evidence/.

## Local Setup
```bash
python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

# Create a .env file (do not commit it):
# RPC_URL="https://YOUR_RPC_URL_HERE"
set -a; source .env; set +a

python src/smoke_latest_block.py
```
