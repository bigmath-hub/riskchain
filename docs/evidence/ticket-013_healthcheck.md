# Ticket 013 - Healthcheck

## Command
```bash
python src/healthcheck_v0.py
```

## Output
```text
db_path=data/riskchain.db ok
cursor_value=1035
last_run_utc=2026-02-03T15:48:35Z
age_seconds=1134 fresh=STALE
latest_block=24377417
```
## Notes
- `last_run_utc` is updated by the watcher once per cycle (after a successful run).
- `fresh` is based on `age_seconds` vs a threshold (default 180 seconds).


