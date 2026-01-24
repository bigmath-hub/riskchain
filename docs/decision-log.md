## 2026-01-20 - Ticket 001 v0
### Business goal (risk question)
- Detect large transfers that may indicate laundering risk.

### Data Source(s)
- Blockchair
- I chose Blockchair because it has a free tier and simple API docs.

### What is "suspicious" (v0 rule)
- Flag if value_eth >= 3 AND wallet_age_days <= 7

### Evidence format
- "A log line with `FLAGGED` + tx hash"
- "A SQLite row in `flagged_txs`"
- "Terminal snippet showing the flagged row from SQLite".

## 2026-01-24
### Closed TICKET#008 — Block Fetch v0 
**Evidence:** docs/evidence/ticket-008_block-fetch.md — Code: 28e926e

