# Master programme

StockPilot AI: 90-Day Supply Chain, Data Analytics and AI Development Programme. Approved version, 22 November 2026.

Related files: [README](README.md) · [Master programme](MASTER_PROGRAMME.md) · [Daily plan](DAILY_STUDY_PLAN.md) · [Progress](PROGRESS_TRACKER.md)

## 1. Facts

| Item | Value |
|---|---|
| Start | Mon 23 Nov 2026 (Day 1) |
| End | Sat 20 Feb 2027 (Day 90) |
| Calendar days | 90 |
| Study days | 78 (six study days, then one rest day; final six days are study days) |
| Rest days | Days 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84 |
| Hours per study day | 4.5 |
| Total study hours | 351 |
| Budget | 0 EUR required, 50 EUR maximum |
| Operating system | Windows 11 |
| Outside the 351 hours | 45 minutes daily for German and job applications |

## 2. Daily time allocation (270 minutes)

| Block | Minutes | Content |
|---|---|---|
| Supply chain concepts | 45 | One concept and one worked example |
| Technical learning | 75 | One technical lesson with live typing |
| Project development | 90 | The day's build task |
| Exercises and documentation | 30 | Exercise and LEARNING_LOG notes. On Saturdays this block holds SQL and Excel practice |
| Review and GitHub update | 30 | Tests, commit, push, PROGRESS_TRACKER.md update |
| **Total** | **270** | 4.5 hours |

Never cut the review block. It holds testing and commits.

## 3. Career outcome

Supply chain plus data analytics plus applied AI. Priority titles: Inventory Analyst, Supply Chain Analyst,
Operations Analyst. Also: Inventory Controller, Inventory Specialist, Replenishment Analyst, Supply Chain Reporting
Analyst, Inventory Planning Analyst, Junior Demand Planner, Supply Chain Systems Analyst.
Detail: [CAREER_ROADMAP.md](CAREER_ROADMAP.md).

The programme adds analytical and AI evidence to 11+ years of operational inventory experience. It does not
qualify anyone for senior planning or AI engineering roles on its own.

## 4. Phases

| Phase | Name | Days | Dates | Study days | Hours |
|---|---|---|---|---|---|
| 1 | Foundations | 1 to 14 | Mon 23 Nov 2026 to Sun 6 Dec 2026 | 12 | 54 |
| 2 | Data analytics | 15 to 28 | Mon 7 Dec 2026 to Sun 20 Dec 2026 | 12 | 54 |
| 3 | Inventory planning engine | 29 to 42 | Mon 21 Dec 2026 to Sun 3 Jan 2027 | 12 | 54 |
| 4 | Forecasting and supply-chain performance | 43 to 56 | Mon 4 Jan 2027 to Sun 17 Jan 2027 | 12 | 54 |
| 5 | StockPilot application and LLM integration | 57 to 70 | Mon 18 Jan 2027 to Sun 31 Jan 2027 | 12 | 54 |
| 6 | AI agent and professional controls | 71 to 84 | Mon 1 Feb 2027 to Sun 14 Feb 2027 | 12 | 54 |
| 7 | Portfolio and career preparation | 85 to 90 | Mon 15 Feb 2027 to Sat 20 Feb 2027 | 6 | 27 |
| | **Total** | 1 to 90 | | **78** | **351** |

### Phase 1. Foundations (Days 1 to 14)

**Learning objective:** Python fundamentals, VS Code and terminal, Git and GitHub, CSV and JSON, SQL fundamentals, inventory terms and KPIs.

**Technical skills:** Python basics, files, exceptions, first pandas, SQLite, pytest, Git.

**Supply chain topics:** SCOR overview, inventory terms, master data, demand patterns, inventory flow, cycle counts.

**Deliverables:**

- DEL-01 Repository and workspace pushed to GitHub (Day 1)
- DEL-02 Data dictionary reviewed, questions logged (Day 6)
- DEL-03 Baseline skills assessment recorded (Day 6)
- DEL-04 Validation and cleaning scripts for the v1 files (Day 12)
- DEL-05 Synthetic data generator v1 (six files) with tests (Day 13)

**Assessment criteria:** At least 10 commits pushed. Generator v1 writes six files. Same seed gives identical files. At least 8 validation checks pass. You explain each file in the repository.

### Phase 2. Data analytics (Days 15 to 28)

**Learning objective:** Analyse inventory data and communicate findings.

**Technical skills:** pandas groupby and merge, SQL joins, CASE, CTEs, window functions, Excel Power Query, Power BI model, DAX.

**Supply chain topics:** Inventory KPI definitions, availability, accuracy, supplier delivery, procure to pay, KPI design.

**Deliverables:**

- DEL-06 Synthetic data generator v2 (five more files) (Day 19)
- DEL-07 Data-quality checks (8 or more) and report (Day 20)
- DEL-08 SQL query set (15 or more queries, cross-checked) (Day 25)
- DEL-09 Power BI dashboard v1 (8 or more KPIs) (Day 27)
- DEL-10 Branch performance report (Day 27)

**Assessment criteria:** 15 or more saved SQL queries checked against pandas. Data-quality report with 8 or more checks. Dashboard with 8 or more KPIs. Model diagram.

### Phase 3. Inventory planning engine (Days 29 to 42)

**Learning objective:** Produce reliable inventory calculations without AI.

**Technical skills:** Cumulative sums, standard deviation, NormalDist, pytest parametrize and approx, integration tests.

**Supply chain topics:** ABC, XYZ, demand variability, lead-time demand, safety stock, service levels, reorder point, EOQ, excess and obsolete stock.

**Deliverables:**

- DEL-11 ABC and XYZ module with tests (Day 31)
- DEL-12 Planning engine: safety stock, reorder point, EOQ, proposals (Day 40)
- DEL-13 Stockout and excess detection (Day 41)
- DEL-14 Calculation test suite (30 or more tests, 5 hand checks) (Day 41)

**Assessment criteria:** Every formula in BUSINESS_RULES.md implemented. 30 or more tests pass. 5 hand checks recorded within 0.01. Proposals produced with no AI.

### Phase 4. Forecasting and supply-chain performance (Days 43 to 56)

**Learning objective:** Identify supply-chain problems and explain their operational impact.

**Technical skills:** Time series in pandas, rolling windows, chronological split, Plotly, report generation.

**Supply chain topics:** Forecasting methods, MAE, WAPE, bias, business impact of error, supplier lead times, procurement TCO and supplier scorecards, root cause, exceptions.

**Deliverables:**

- DEL-15 Forecast module (naive, moving average, smoothing, metrics) with tests (Day 48)
- DEL-16 Forecast comparison report (Day 50)
- DEL-17 Supplier performance analysis (Day 52)
- DEL-18 Inventory exception report (Day 55)
- DEL-19 Project 3 case study draft (final version Day 88) (Day 55)

**Assessment criteria:** Chronological split. Naive baseline plus at least two methods. MAE, WAPE, bias reported. Supplier report. Exception report. Project 3 draft.

### Phase 5. StockPilot application and LLM integration (Days 57 to 70)

**Learning objective:** Run a working inventory application with an AI assistant.

**Technical skills:** Streamlit, app structure, SQLite access layer, logging, APIs, environment variables, Pydantic, structured outputs, prompts.

**Supply chain topics:** ERP and MRP basics, planning reviews, returns and reverse logistics, briefings, evidence-based reporting.

**Deliverables:**

- DEL-20 App skeleton, CSV upload and dashboard page (Day 60)
- DEL-21 Forecasting and planning pages (Day 61)
- DEL-22 AI provider layer: mock provider and optional Claude provider (Day 67)
- DEL-23 AI briefing with evidence records and claim checker (Day 69)

**Assessment criteria:** App starts from a clean clone with one command. Mock mode needs no key. 10 briefings with zero unsupported numbers. API errors handled.

### Phase 6. AI agent and professional controls (Days 71 to 84)

**Learning objective:** Investigate problems with a controlled agent, with a person approving every action.

**Technical skills:** Tool calling, JSON schemas, agent loop, limits, approval state, audit log, evaluation, prompt injection.

**Supply chain topics:** Replenishment controls, transport modes and freight, Incoterms 2020, customs documents and landed cost, approval in purchasing, audit trails, risk and resilience.

**Deliverables:**

- DEL-24 Six agent tools with Pydantic models and tests (Day 75)
- DEL-25 Agent controller with limits (Day 76)
- DEL-26 Approval workflow and audit log (Day 79)
- DEL-27 Security tests: prompt injection and secrets (Day 81)
- DEL-28 Evaluation set (40 cases) run and results recorded (Day 83)

**Assessment criteria:** Six tools validated. 40 evaluation cases run. Tool choice correct in 90 percent or more. Zero unsupported numbers. 5 or more injection tests pass. Every decision audited.

### Phase 7. Portfolio and career preparation (Days 85 to 90)

**Learning objective:** Make the work ready to show employers.

**Technical skills:** Architecture diagrams, documentation checks, screen recording.

**Supply chain topics:** Explaining SCOR, KPIs and results to managers; interview preparation.

**Deliverables:**

- DEL-29 Final README, architecture diagram and documentation (Day 86)
- DEL-30 Test and evaluation report (Day 87)
- DEL-31 Power BI documentation and screenshots; Project 3 final (Day 88)
- DEL-32 Demo video (3 to 5 minutes) (Day 89)
- DEL-33 CV text, LinkedIn text, interview presentation (Day 90)

**Assessment criteria:** README, diagram, data dictionary, formulas, test and evaluation report, screenshots, 3 to 5 minute video, CV and LinkedIn text, 10-minute presentation.


## 5. Three projects

| Project | Description | Main folders |
|---|---|---|
| 1. StockPilot AI | Multi-branch inventory intelligence and replenishment app with an AI analyst, six-tool agent and approval workflow | `src/`, `app/`, `tests/`, `evals/` |
| 2. Supply Chain Performance Dashboard | Power BI report on the same synthetic company | `dashboard/` |
| 3. Demand Forecasting Case Study | Python study comparing naive, moving average and exponential smoothing with a chronological split | `notebooks/` |

## 6. Rules

1. All data is synthetic. Label all results as simulated.
2. Python calculates every number. The LLM never calculates or invents numbers.
3. Every numerical claim in an AI answer carries an evidence record (source tool, business rule, returned result, dataset and record).
4. No automatic purchase orders. No supplier contact. A person approves every proposal.
5. The mock AI provider works without an API key at all times.
6. One lesson at a time. A milestone is verified before the next starts.
7. No silent changes. Changes go through [DECISIONS_LOG.md](DECISIONS_LOG.md).
8. Behind schedule: cut optional features in the order in [RISKS_AND_RECOVERY.md](RISKS_AND_RECOVERY.md). Never cut testing or documentation.

## 7. Technology stack

| Purpose | Tool |
|---|---|
| Programming | Python, pandas, NumPy |
| Database | SQLite, SQL |
| Application | Streamlit |
| Charts | Plotly |
| Business intelligence | Power BI Desktop |
| Validation | Pydantic |
| Testing | pytest |
| AI | Mock provider (default), Claude API provider (optional) |
| Development | VS Code, PowerShell, Git, GitHub, Claude Code |

## 8. Budget

| Item | Cost |
|---|---|
| Courses and documentation | 0 EUR |
| Python, VS Code, Git, GitHub, SQLite, Streamlit, Plotly, pytest, Pydantic, Power BI Desktop | 0 EUR |
| Claude Code | Included in the existing Claude Pro plan (D-021). Pro usage limits apply |
| Claude API calls | Not used (D-022). Mock provider only |
| Certificates | 0 EUR. Paid certificates postponed |

A Claude subscription and API usage are billed separately. The programme runs at 0 EUR extra: Claude Code on Pro, the app in mock mode.

## 9. Evidence status on 15 January 2027 (Day 54)

Day 54 is Friday 15 January 2027. Day 56 is a rest day. Phase 4 closes on Day 55. On Day 54, only deliverables due
on or before Day 54 count as complete. On Day 54 the real status is recorded in PROGRESS_TRACKER.md.

| ID | Deliverable | Due | Status on Day 54 |
|---|---|---|---|
| DEL-01 | Repository and workspace pushed to GitHub | Day 1 | Complete, if on schedule |
| DEL-02 | Data dictionary reviewed, questions logged | Day 6 | Complete, if on schedule |
| DEL-03 | Baseline skills assessment recorded | Day 6 | Complete, if on schedule |
| DEL-04 | Validation and cleaning scripts for the v1 files | Day 12 | Complete, if on schedule |
| DEL-05 | Synthetic data generator v1 (six files) with tests | Day 13 | Complete, if on schedule |
| DEL-06 | Synthetic data generator v2 (five more files) | Day 19 | Complete, if on schedule |
| DEL-07 | Data-quality checks (8 or more) and report | Day 20 | Complete, if on schedule |
| DEL-08 | SQL query set (15 or more queries, cross-checked) | Day 25 | Complete, if on schedule |
| DEL-09 | Power BI dashboard v1 (8 or more KPIs) | Day 27 | Complete, if on schedule |
| DEL-10 | Branch performance report | Day 27 | Complete, if on schedule |
| DEL-11 | ABC and XYZ module with tests | Day 31 | Complete, if on schedule |
| DEL-12 | Planning engine: safety stock, reorder point, EOQ, proposals | Day 40 | Complete, if on schedule |
| DEL-13 | Stockout and excess detection | Day 41 | Complete, if on schedule |
| DEL-14 | Calculation test suite (30 or more tests, 5 hand checks) | Day 41 | Complete, if on schedule |
| DEL-15 | Forecast module (naive, moving average, smoothing, metrics) with tests | Day 48 | Complete, if on schedule |
| DEL-16 | Forecast comparison report | Day 50 | Complete, if on schedule |
| DEL-17 | Supplier performance analysis | Day 52 | Complete, if on schedule |
| DEL-18 | Inventory exception report | Day 55 | Partial: work in progress on Day 54 |
| DEL-19 | Project 3 case study draft (final version Day 88) | Day 55 | Partial: work in progress on Day 54 |

Not available on Day 54: the application (Phase 5), the AI briefing, the agent and approval workflow.

**Evidence usable in applications on Day 54:** public repository, synthetic dataset and generator, validation scripts,
SQL query set, Power BI dashboard and branch report, tested planning engine, forecast module and comparison report,
supplier analysis. Exception report and Project 3 are work in progress.

## 10. Weekly assessment

Each Saturday: a 20-minute quiz on the week, the milestone checklist and a PROGRESS_TRACKER.md review.
Each phase ends with the acceptance criteria above.
