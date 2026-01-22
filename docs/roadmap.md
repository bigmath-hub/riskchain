## M1 — Due Diligence

**Goal:** Define the project risk question and the minimum proof artifacts.

**Ticket count:** 2–4

**Definition of Done:**
- `docs/decision-log.md` has 1 entry with: risk question, data source, suspicious rules (v0), and evidence format.
- `docs/glossary.md` has 8–12 terms (English + short PT meaning).
- `docs/runbook.md` has a "How to run (local)" placeholder.
- One commit is pushed to `main` with these docs.

**Evidence:**
- Terminal output: `ls -la docs/` shows the files.
- Terminal output: `git log -1 --oneline` shows the commit hash.

## M2: Whale Watcher v1 (24/7 logging to DB)
**Goal:** Monitor large on-chain transactions on Ethereum and store them in a local database.

**Ticket count:** 4-8

**Definition of Done:**
- A watcher script exists in `src/whale_watcher.py`
- The watcher uses the same data source defined in M1 to read new blocks/transactions.
- A simple rule exists: "large transaction" = value >= threshold (configurable).
- Each match is written to SQLite (tx hash, timestamp, from, to, value, rule_id).
- A 24/7 runner is documented (systemd or cron) and `docs/runbook.md` explains start/stop + where logs/DB are.

**Evidence:**
- Terminal output shows recent log lines with at least 1 detected event.
- Terminal output shows SQLite rows exist (count > 0) and a sample row.


## M3 — Forensics Notebook (historic hack flow)

**Goal:** Analyze one historic crypto incident and explain the money flow with simple charts and notes.

**Ticket count:** 3–6

**Definition of Done:**
- One notebook exists at `notebooks/forensics_case_v1.ipynb`.
- The notebook loads a dataset from `data/` (CSV or JSON) with transaction-level fields.
- Running the notebook produces 2–3 simple visuals (for example: top receivers, timeline volume, transaction size distribution).
- The notebook ends with a short "Findings" section and a short "Limitations" section (B1 English).
- One evidence file exists in `docs/evidence/` with a screenshot of at least one chart.

**Evidence:**
- Screenshot of the notebook output (at least one chart).
- Terminal output: `ls -la notebooks/` shows the notebook file.

## M4 — Mock Audit Report + Pitch

**Goal:** Create a mock audit report and a short pitch for reviewers.

**Ticket count:** 3–5

**Definition of Done:**
- One audit report exists at `docs/audit-report.md`.
- One risk register table exists at `docs/risk-register.md`.
- One recommendations section exists (inside the report or as `docs/recommendations.md`).
- The report links to key evidence from M2 and M3 (files or commands).
- One evidence file exists in `docs/evidence/` with a screenshot of one finding or recommendation.

**Evidence:**
- `ls -la docs/` shows the report files.
- Screenshot stored in `docs/evidence/` (one finding or recommendation).
