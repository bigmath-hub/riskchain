# TICKET#006 - Storage Layer v0 (SQLite)

## Commands
```bash
sqlite3 data/riskchain.db ".databases"
ls -la data/riskchain.db
sqlite3 data/riskchain.db ".schema transactions"
sqlite3 data/riskchain.db "INSERT OR IGNORE INTO transactions (tx_hash, block_number, from_address, to_address, value_wei, timestamp_utc) VALUES ('0xSAMPLE_TX_HASH', 1, '0xFROM', '0xTO', 123, '2026-01-22T00:00:00Z');"
sqlite3 data/riskchain.db "SELECT COUNT(*) FROM transactions;"
python src/db_bootstrap.py
```

## Output
```
total 20
drwxrwxr-x 2 matheus matheus  4096 Jan 22 23:02 .
drwxrwxr-x 8 matheus matheus  4096 Jan 22 22:41 ..
-rw-r--r-- 1 matheus matheus 12288 Jan 22 23:02 riskchain.db

CREATE TABLE transactions (tx_hash TEXT UNIQUE, block_number INTEGER, from_address TEXT, to_address TEXT, value_wei INTEGER, timestamp_utc TEXT);                                         

1

connected=data/riskchain.db
cols=6
rows=1
```
## Git commit:
- faf0e3e
