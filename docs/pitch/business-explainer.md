# RiskChain — Business Explainer (Plain Language)

## What this project is (simple summary)
- RiskChain is my 90-day portfolio project to learn by doing in blockchain risk and basic forensics.
- In simple terms: I build a small monitoring and analysis workflow that helps notice unusual transaction activity and document it with clear proof.
- I am a beginner with zero professional tech experience, so I keep the scope small and evidence-driven.

---

## 1) 5W2H (What / Why / Who / Where / When / How / How much)

### What
- A small, repeatable workflow that:
  - collects public transaction data,
  - flags “unusual” activity using simple rules,
  - stores results in a database,
  - and produces audit-style evidence (logs, screenshots, and short notes).

### Why
- Because financial risk work needs two things:
  - early signals (so teams can investigate),
  - and proof (so decisions are explainable later).
- I want a portfolio that shows structured thinking, careful documentation, and basic automation.

### Who
- Primary user: me (learning project).
- Intended audience: a non-technical reviewer, a junior hiring manager, or a risk team that wants to see my thinking.
- Stakeholders in real life: compliance teams, fraud teams, monitoring teams, and auditors.

### Where
- The data is public (blockchain transaction data).
- The project runs locally on Linux (a common operating system used on servers).

### When
- Built over 90 days with small weekly milestones.
- Designed to run continuously (like a basic monitoring job).

### How
- I use small scripts and simple storage:
  - Python (a beginner-friendly programming language) for data handling,
  - SQL (a simple way to query a database) for storage and retrieval,
  - notebooks (interactive documents) for analysis and explanation.
- I document every decision and keep evidence for each milestone.

### How much (realistic ranges)
- Time: ~5 to 10 hours per week for 90 days.
- Cost: low-cost learning setup (often free public data + free tools).
- Main “cost” is discipline: writing notes, saving evidence, and improving clarity.

---

## 2) Practical applicability (real-world problems it helps solve)
RiskChain is a learning version of work that exists in many companies:

- Fraud detection:
  - spotting unusual movement patterns that may indicate scams or stolen funds.
- Compliance monitoring:
  - helping teams notice suspicious activity and keep a record of why something was reviewed.
- Ongoing monitoring:
  - watching large movements and anomalies so analysts can investigate faster.
- Audit evidence:
  - producing clear, repeatable proof of what was observed and how it was flagged.
- Investigation support:
  - organizing data so an analyst can answer: “what happened, when, and where did funds go next?”

Where this kind of work is used:
- Exchanges and custody platforms.
- Fintech and payment companies.
- Banks and financial risk teams exploring crypto exposure.
- Compliance and analytics teams that support investigations.

Two simple examples:
- Fraud-like example:
  - A wallet suddenly receives funds from many small senders and then quickly sends one large transfer out. This can be a sign of scam collection or stolen funds being moved. RiskChain would flag it for review and keep a clear record of why it was flagged.
- Compliance-like example:
  - A business wants basic monitoring and reporting for large transfers and unusual activity, similar to how an accounting team reviews unusual journal entries. RiskChain helps create a consistent trail: what was seen, when it happened, and what rule triggered the review.

---

## 3) Skills acquired (simple, grouped)
This project is designed to show entry-level skills in a practical way:

### Data handling (basic)
- Query results to answer simple questions (what, when, how often).

### Documentation and evidence
- Keep evidence artifacts (logs, screenshots, small reports).
- Make results repeatable (not “it worked once”).

### Basic automation
- Run scripts on a schedule.
- Keep simple monitoring logs.

### Structured thinking
- Define what “suspicious” means in plain rules (version 0).
- Separate signal vs. proof: a flag is not an accusation, it is a reason to review.

### Communication
- Explain the work without jargon.
- Summarize findings with clear limitations.

Tools (examples only):
- Python (to process data), Linux (to run tasks), SQL (to query stored data), notebooks (to explain analysis).

---

## 4) Entry-level roles this project supports (and why)
Below are realistic beginner roles where this kind of project is relevant:

- Junior Risk Analyst:
  - Reviews risk signals and helps document decisions. RiskChain shows structured review and evidence habits.
- Fraud Analyst (entry-level):
  - Looks for unusual patterns and escalates cases. RiskChain shows how to define simple flags and track findings.
- Compliance Analyst (entry-level):
  - Supports monitoring and record-keeping. RiskChain emphasizes explainable evidence and traceability.
- Blockchain Analyst (junior):
  - Studies on-chain activity and basic flows. RiskChain shows practical data handling and simple investigation thinking.
- Monitoring Analyst / SOC Analyst (junior):
  - Watches alerts and triages issues. RiskChain mirrors alerting + logging + escalation mindset.
- Data Analyst Intern:
  - Turns data into clear summaries. RiskChain demonstrates cleaning, querying, and explaining results.

Two roles I am targeting now:
- Blockchain Analyst (junior):
  - I like investigation work. I want to understand transaction flows and explain findings clearly. RiskChain trains this skill with simple rules and strong documentation.
- Fraud Analyst (entry-level):
  - I want to learn how monitoring and triage works in real teams. RiskChain is relevant because it practices “signal + evidence” and careful communication.

Long-term direction (not my current level yet):
- Blockchain engineering and smart contract review:
  - I want to move toward building and reviewing blockchain software. For now, RiskChain is my foundation in risk thinking, data discipline, and evidence habits.

---

## 5) “How I would explain this on Day 1 at a company” (8–12 lines)
Hi everyone, I’m Matheus. I’m early in my career and I’m building RiskChain as a learning project.
The goal is simple: practice how to notice unusual transaction activity and document it clearly.
I collect public transaction data, apply a few basic rules to flag unusual patterns, and store results for review.
I treat every flag as a starting point for investigation, not a final claim.
I focus on repeatable runs, clear logs, and simple written evidence so someone else can review my work.
This project helps me practice disciplined thinking: define “suspicious,” keep proof, and communicate without jargon.
Over time I plan to improve the rules, add better summaries, and keep a clear decision log.
I would love feedback on what your team considers the most useful signals and what “good evidence” looks like in your process.

---

## 6) No-jargon rule (how I keep it understandable)
- If I must use a technical term, I define it right away in simple words.
- I prefer concrete language.

Additional limitations:
- I use an AI assistant as a study guide (a tool that helps me learn and plan).
