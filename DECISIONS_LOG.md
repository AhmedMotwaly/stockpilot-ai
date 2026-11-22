# Decisions log

Important decisions and why they were made. Never change an approved decision silently: add a new entry that
references the old one. Related: [MASTER_PROGRAMME.md](MASTER_PROGRAMME.md), [RISKS_AND_RECOVERY.md](RISKS_AND_RECOVERY.md).

## Decisions

| ID | Date | Decision | Reason | Status |
|---|---|---|---|---|
| D-001 | 22 Nov 2026 | Programme frame: 90 days, 23 Nov 2026 to 20 Feb 2027, 78 study days, 351 hours | Approved programme | Approved |
| D-002 | 22 Nov 2026 | Daily split 45/75/90/30/30 minutes (270) | Earlier split added up to 300 minutes | Approved |
| D-003 | 22 Nov 2026 | German and job applications 45 minutes daily, outside the 351 hours | Permit deadline and job search continue | Approved |
| D-004 | 22 Nov 2026 | Saturday SQL and Excel practice inside the 30-minute exercise block | No extra hours | Approved |
| D-005 | 22 Nov 2026 | Three projects: StockPilot AI, Power BI dashboard, forecasting case study | Approved scope | Approved |
| D-006 | 22 Nov 2026 | Six agent tools, one controlled agent, no multi-agent design | Simpler to test and explain | Approved |
| D-007 | 22 Nov 2026 | Python performs all calculations; evidence record for every number | Prevent invented numbers | Approved |
| D-008 | 22 Nov 2026 | Human approval mandatory; no purchase orders, no supplier contact | Safety and realism | Approved |
| D-009 | 22 Nov 2026 | Mock AI provider is the default; Claude API optional and approved per expense | Budget 50 EUR | Approved |
| D-010 | 22 Nov 2026 | Claude Code is the development assistant | User approval 22 Nov 2026 | Approved |
| D-011 | 22 Nov 2026 | Synthetic data only; dataset built in two stages (Day 13 and Day 19) | Phase 1 load | Approved |
| D-012 | 22 Nov 2026 | Day 54 (15 Jan 2027) evidence checkpoint; Day 55 deliverables counted as partial | Correct milestone statement | Approved |
| D-013 | 22 Nov 2026 | Added src/approval/, src/reporting/ and database/queries/ to the starting folder list | Keep approval and reporting separate from AI code, as the architecture requires; keep saved SQL with the database files instead of a new top-level folder | Approved 22 Nov 2026 |
| D-014 | 22 Nov 2026 | Progress files: PROGRESS_TRACKER.md and DECISIONS_LOG.md replace PROGRESS.md and DECISIONS.md from the earlier prompt | Final modification lists these names | Approved |
| D-015 | 22 Nov 2026 | LEARNING_LOG.md, CHANGELOG.md and lesson notes in docs/lessons/ are created on Day 1; test results live in TESTING_AND_EVALUATION.md section 9 | Avoid empty files before they are needed | Approved 22 Nov 2026 |
| D-016 | 22 Nov 2026 | Evaluation set expanded to 40 cases | Final modification | Approved |
| D-017 | 22 Nov 2026 | Safety stock rules: fixed and variable lead time; service by cycle service level; fill rate reported separately | Master prompt Part 8 | Approved |
| D-018 | 22 Nov 2026 | Supplier orders planned at WH01 from total demand; branch transfer suggestions optional | Keeps version 1 manageable | Approved |
| D-019 | 22 Nov 2026 | Phase tags v0.1 to v0.6 and v1.0 | Consistent release points | Approved 22 Nov 2026 |
| D-020 | 22 Nov 2026 | warehouse_activity.csv added on Day 19 for the productivity KPI in Project 2 | Project 2 needs a workload table | Approved 22 Nov 2026 |
| D-021 | 22 Nov 2026 | Claude Code runs on the user's Claude Pro plan. No Console or API billing | User answer to O-001 | Approved |
| D-022 | 22 Nov 2026 | No Claude API use. The mock provider is the only live provider. The Claude provider is still written on Day 67 and tested with a fake client, never called live. The 40-case evaluation runs in mock mode only | User answer to O-002. A Pro subscription does not include API usage | Approved |
| D-023 | 22 Nov 2026 | CV fact: the eXtra network was 3 stores and 1 distribution center. The 55-store figure is removed. The Amazon 20 percent error-reduction figure is removed (not confirmed) | User answer to O-004 | Approved |
| D-024 | 22 Nov 2026 | Days 33 (25 Dec 2026) and 40 (1 Jan 2027) stay study days | User answer | Approved |
| D-025 | 22 Nov 2026 | Added CLAUDE.md so Claude Code reads the programme rules at the start of every session | Claude Code loads CLAUDE.md automatically; keeps lessons consistent across sessions | Approved with this log |
| D-026 | 23 Nov 2026 | Repository licence is MIT. LICENSE file added at the project root on Day 1 | Simple, open, portfolio-friendly; anyone may reuse the code with attribution. Closes O-003 | Approved by learner 23 Nov 2026 |

## Open items

| ID | Question | Answer (22 Nov 2026) |
|---|---|---|
| O-001 | Claude Code access and cost | Claude Pro plan. See D-021 |
| O-002 | Claude API spending | None. Mock mode only. See D-022 |
| O-003 | Licence for the repository | Closed: MIT chosen on Day 1. See D-026 |
| O-004 | 55-store and Amazon 20 percent figures | 3 stores and 1 distribution center; both figures removed. See D-023 |
| O-005 | Approve D-013, D-015, D-019, D-020 | Approved |
| O-006 | Days 33 and 40 on public holidays | Keep. See D-024 |

## Change template

```
| D-0NN | date | Decision | Reason | Replaces D-0xx |
```
