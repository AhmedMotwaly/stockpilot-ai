# GitHub portfolio plan

How the work becomes public proof. Architecture: [PROJECT_ARCHITECTURE.md](PROJECT_ARCHITECTURE.md).
Career use: [CAREER_ROADMAP.md](CAREER_ROADMAP.md).

## 1. Repository

| Item | Value |
|---|---|
| Repository name | stockpilot-ai |
| Local folder | StockPilot-AI |
| Visibility | Public from Day 1, after `.gitignore` and `.env.example` are committed |
| Default branch | main |
| Licence | MIT proposed (decide on Day 1) |

Folder layout: see PROJECT_ARCHITECTURE.md section 3.

## 2. Commit strategy

- Commit at least once per study day, at the end of the review block.
- One logical change per commit. Run tests before committing.
- Message format: `type: short description`. Types: feat, fix, test, docs, data, refactor, chore.
  Examples: `feat: add safety stock for variable lead time`, `test: hand check BR-07 example`.
- Tags at phase ends: v0.1 (Day 13), v0.2 (Day 27), v0.3 (Day 41), v0.4 (Day 55), v0.5 (Day 69), v0.6 (Day 83), v1.0 (Day 90).
- Before every push: `git status`, check no `.env`, no database file, no generated data.

## 3. Documentation requirements

README with purpose, simulated-data notice, features, architecture diagram, Windows install steps, run steps,
mock and live mode, tests, evaluation results, limits, roadmap. Plus the project documentation files in the root,
a data dictionary, formula documentation, test and evaluation report, Power BI measure notes.

## 4. Screenshots (folder `screenshots/`)

1. Upload page with a validation error.
2. Inventory dashboard.
3. ABC/XYZ matrix.
4. Forecast comparison chart.
5. Exception list.
6. AI briefing with evidence links.
7. Agent answer to the stockout question.
8. Approval screen and audit history.
9. Power BI overview page.
10. Test run output.

No screenshot may show a key, a real name or real company data.

## 5. Demo preparation (3 to 5 minutes)

1. Problem in one sentence.
2. Upload sample data; show one validation message.
3. Dashboard and one exception.
4. Ask the agent the stockout question.
5. Show the evidence behind one number.
6. Approve one proposal, reject one with a reason.
7. Show the audit entry.
8. Close with tests and evaluation numbers.

## 6. Portfolio presentation (10 minutes)

Problem, data, architecture, planning rules, forecasting results, AI controls, evaluation, limits, what you learned.

## 7. CV project description (draft, update with real numbers on Day 90)

StockPilot AI (personal project, synthetic data, 2026 to 2027). Built a Python and Streamlit inventory planning
application for a simulated 10-store retailer: data validation, SQL analysis, ABC/XYZ, safety stock, reorder point,
EOQ, demand forecasting with error measurement, and an AI assistant that calls six tested tools, cites evidence for
every number and requires human approval for replenishment proposals. [N] automated tests; [N]-case AI evaluation.

## 8. Interview preparation

Questions to answer from this repository: why Python does the maths, how the claim checker works, why WAPE instead
of MAPE, what the safety stock assumptions are, what happens when the API fails, how approval is enforced, what the
limits are. Full list: CAREER_ROADMAP.md section 6.
