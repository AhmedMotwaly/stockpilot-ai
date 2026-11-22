# StockPilot AI

Inventory intelligence and replenishment assistant for a fictional multi-branch retailer.
Portfolio project built during a 90-day supply chain, data analytics and applied AI programme.

> **Simulated data.** Every dataset, company, branch, supplier and result in this repository is synthetic.
> Nothing comes from a real employer.

## Project status

| Item | Status |
|---|---|
| Planning and documentation | Complete (22 Nov 2026) |
| Day 1 | Starts Monday 23 November 2026, after approval |
| Application code | Not started. Code is added phase by phase |
| Current version | v0.0 (documentation only) |

Progress is recorded in [PROGRESS_TRACKER.md](PROGRESS_TRACKER.md).

## Business problem

Retail inventory teams track thousands of SKUs across many branches. Stockouts lose sales. Excess stock ties up cash.
Teams often work from exports and spreadsheets, find problems late, and struggle to explain why a replenishment
quantity is right.

StockPilot AI shows how a planner moves from raw files to tested calculations, clear exceptions and replenishment
proposals, with an AI assistant explaining the results and a person approving every action.

## Objectives

1. Turn raw inventory and sales files into validated, consistent data.
2. Calculate inventory KPIs and planning values with tested Python code.
3. Forecast demand and measure forecast error against a simple baseline.
4. Flag stockout risk, excess stock and data problems.
5. Explain results through an AI analyst that only uses numbers returned by approved tools.
6. Keep a person in control: every replenishment proposal needs human approval, and every decision is logged.

## Main features (planned)

| Module | Feature | Phase |
|---|---|---|
| A | Data ingestion and validation | 1 and 5 |
| B | Inventory analytics and branch comparison | 2 |
| C | ABC and XYZ classification | 3 |
| D | Demand analysis and forecasting | 4 |
| E | Inventory planning: safety stock, reorder point, EOQ, proposals | 3 |
| F | Exception management | 4 |
| G | AI inventory analyst with evidence records | 5 |
| H | Tool-using AI agent with six approved tools | 6 |
| I | Human approval and audit trail | 6 |
| J | Reports and CSV downloads | 4 to 6 |

The AI layer never sends purchase orders, never contacts suppliers and never calculates numbers itself.

## Three portfolio projects

1. **StockPilot AI**: this application.
2. **Supply Chain Performance Dashboard**: Power BI report on the same synthetic company (folder `dashboard/`).
3. **Demand Forecasting Case Study**: Python study comparing forecast methods (folder `notebooks/`).

## Technology stack

Python, pandas, NumPy, SQLite, SQL, Streamlit, Plotly, Power BI Desktop, Pydantic, pytest, Git and GitHub.
AI: a mock provider (free, no key). A Claude API provider is written and tested with a fake client but not called
live in this project (DECISIONS_LOG.md, D-022). Claude Code is the development assistant and is not part of the application.

## Architecture overview

```
CSV files -> validation -> SQLite -> Python business logic (no AI)
          -> six approved tools -> agent controller -> AI provider (mock or Claude)
          -> briefing with evidence and claim check -> human approval -> audit log and reports
          -> Streamlit interface
```

Full detail: [PROJECT_ARCHITECTURE.md](PROJECT_ARCHITECTURE.md).

## Installation (Windows 11)

Run these in **PowerShell**, inside the project folder. Day 1 explains each step.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If PowerShell refuses to run `Activate.ps1`, run this once, then activate again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Copy `.env.example` to `.env`. Keep the provider on `mock` unless you approve API spending.

## How to run the application

The application does not exist yet. From Phase 5 (Day 57) onward:

```powershell
streamlit run app/main.py
```

Tests (from Day 8 onward):

```powershell
python -m pytest
```

## Day 1 preparation checklist

- [x] Python installed: 3.11.15 (checked 22 Nov 2026)
- [x] Git installed: 2.54.0 (checked 22 Nov 2026)
- [ ] VS Code installed (1.141.0, checked) with the Python extension (check on Day 1)
- [x] Claude Code runs: 2.1.183 on the Claude Pro plan (checked 22 Nov 2026)
- [ ] GitHub account created and you can sign in
- [x] Git name and email set (checked 22 Nov 2026)
- [x] This folder opens in VS Code
- [ ] You read MASTER_PROGRAMME.md sections 1 to 3 and DAILY_STUDY_PLAN.md Week 1
- [x] Open items in DECISIONS_LOG.md answered (22 Nov 2026; licence decided on Day 1)

## Documentation map

| File | Purpose |
|---|---|
| [MASTER_PROGRAMME.md](MASTER_PROGRAMME.md) | The approved 90-day programme |
| [DAILY_STUDY_PLAN.md](DAILY_STUDY_PLAN.md) | Master schedule: all 90 days |
| [PROGRESS_TRACKER.md](PROGRESS_TRACKER.md) | Record of actual progress |
| [SKILLS_MATRIX.md](SKILLS_MATRIX.md) | Current and target skill levels |
| [PROJECT_ARCHITECTURE.md](PROJECT_ARCHITECTURE.md) | System design |
| [DATA_DICTIONARY.md](DATA_DICTIONARY.md) | Every dataset and field |
| [BUSINESS_RULES.md](BUSINESS_RULES.md) | Formulas, assumptions, worked examples |
| [TESTING_AND_EVALUATION.md](TESTING_AND_EVALUATION.md) | Test plan and 40 AI evaluation cases |
| [GITHUB_PORTFOLIO_PLAN.md](GITHUB_PORTFOLIO_PLAN.md) | Repository, commits, demo, CV text |
| [CAREER_ROADMAP.md](CAREER_ROADMAP.md) | Target roles, gaps, interview preparation |
| [DAILY_LESSON_TEMPLATE.md](DAILY_LESSON_TEMPLATE.md) | Structure of every lesson |
| [DECISIONS_LOG.md](DECISIONS_LOG.md) | Approved decisions and changes |
| [RISKS_AND_RECOVERY.md](RISKS_AND_RECOVERY.md) | Risks, recovery steps, cut order |
| [CLAUDE.md](CLAUDE.md) | Rules Claude Code reads at the start of every session |

## Licence and author

Licence: to be chosen on Day 1 (MIT proposed, see DECISIONS_LOG.md).
Author: Ahmad Motwaly.
