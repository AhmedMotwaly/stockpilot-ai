# Project architecture

Approved design for StockPilot AI. Data fields: [DATA_DICTIONARY.md](DATA_DICTIONARY.md).
Formulas: [BUSINESS_RULES.md](BUSINESS_RULES.md). Tests: [TESTING_AND_EVALUATION.md](TESTING_AND_EVALUATION.md).

## 1. Principle

Python business logic works without the LLM. The AI layer only calls approved tools, explains their results and asks
for approval. Every number shown to a user comes from Python.

## 2. System architecture

```
 CSV files (upload or data/sample)
        |
 [Ingestion]  file type, size, column names                 src/data
        |
 [Validation] types, ranges, keys, dates, balances           src/data
        |
 [Database]   SQLite access layer, fixed queries only        src/data, database/
        |
 [Business logic, no AI]                                     src/analytics, src/inventory, src/forecasting
   analytics | classification | demand | forecasting | planning | exceptions
        |
 [Tools]      six approved functions, Pydantic in and out    src/ai/tools
        |
 [Agent controller] tool limit, timeout, argument and result validation   src/ai/agent
        |
 [Provider interface]  Mock | Claude                         src/ai/providers
        |
 [Analyst]    briefing, evidence records, claim checker      src/ai/analyst
        |
 [Approval]   proposed -> approved | rejected                src/approval
        |
 [Audit log and reports]                                     src/approval, src/reporting
        |
 [Streamlit interface]                                       app/
```

## 3. Components and folders

| Folder | Holds | Phase |
|---|---|---|
| `src/data/` | Generator, ingestion, validation, SQLite access | 1, 2, 5 |
| `src/analytics/` | KPIs, branch comparison, supplier metrics | 2, 4 |
| `src/inventory/` | ABC, XYZ, safety stock, reorder point, EOQ, proposals, stockout risk, excess, exceptions | 3, 4 |
| `src/forecasting/` | Data preparation, naive, moving average, smoothing, metrics | 4 |
| `src/ai/` | Providers, tools, agent controller, analyst, evidence, claim checker | 5, 6 |
| `src/approval/` | Approval workflow and audit log | 6 |
| `src/reporting/` | CSV and markdown reports | 4 to 6 |
| `src/utils/` | Shared helpers: configuration, logging, dates | 1 onward |
| `app/` | Streamlit pages | 5, 6 |
| `database/` | SQLite file (ignored by Git), schema SQL and saved queries | 2 onward |
| `database/queries/` | Saved analysis queries | 2 |
| `scripts/` | Command-line entry points, for example the generator | 1 onward |
| `tests/` | pytest tests | 1 onward |
| `evals/` | AI evaluation cases and results | 6 |
| `dashboard/` | Power BI file, model diagram, measure notes | 2, 7 |
| `notebooks/` | Project 3 forecasting case study | 4, 7 |
| `docs/` | Architecture diagram, lesson notes, guides | All |
| `screenshots/` | Images for README and portfolio | 7 |
| `logs/` | Runtime logs (ignored by Git) | 5 onward |
| `data/sample/` | Small synthetic sample, committed | 1 onward |
| `data/generated/` | Full generated data, ignored by Git | 1 onward |

`src/approval/`, `src/reporting/` and `database/queries/` refine the starting folder list. Reason recorded in
DECISIONS_LOG.md (D-013). Git does not track empty folders; each folder appears on GitHub once its first file exists.

## 4. Data flow

1. The generator writes CSV files to `data/generated/` with a fixed random seed.
2. Validation checks each file and writes a data-quality report.
3. The loader writes valid data to SQLite.
4. Business logic reads from SQLite through fixed queries and returns pandas tables.
5. Tools wrap business logic functions and return typed results plus evidence records.
6. The agent picks tools; the provider writes text; the claim checker compares every number with the evidence.
7. Proposals enter the approval queue. A person approves or rejects with a reason.
8. The audit log stores the question, tools, arguments, result fingerprint, text, decision and cost.

## 5. Database structure

Source tables mirror the CSV files in DATA_DICTIONARY.md section 2. Application tables (section 4 of that file):
`proposals`, `decisions`, `audit_log`, `evidence`. Primary and foreign keys follow the data dictionary.
The agent has no SQL access. Only fixed queries in `src/data/` touch the database.

## 6. Python modules (planned)

| Module | Main functions | Rule IDs | Day |
|---|---|---|---|
| `src/data/generate.py` | build_products, build_sales, simulate_stock | | 8 to 19 |
| `src/data/validate.py` | check_columns, check_keys, check_dates, check_balances | | 12 |
| `src/analytics/kpis.py` | inventory_value, turnover, days_of_inventory, availability, accuracy | BR-10, BR-11 | 16 to 25 |
| `src/inventory/classification.py` | abc_class, xyz_class, abc_xyz_matrix | BR-01, BR-02 | 29 to 31 |
| `src/inventory/demand_stats.py` | average_demand, demand_std, lead_time_demand | BR-03, BR-04 | 32 |
| `src/inventory/safety_stock.py` | safety_stock_fixed_lt, safety_stock_variable_lt | BR-05, BR-06 | 33 |
| `src/inventory/reorder.py` | reorder_point, order_up_to | BR-07 | 34 |
| `src/inventory/eoq.py` | economic_order_quantity | BR-08 | 36 |
| `src/inventory/replenishment.py` | suggested_order_qty, build_proposals | BR-09 | 37 |
| `src/inventory/risk.py` | stockout_probability, excess_units | BR-12, BR-13 | 38 to 39 |
| `src/forecasting/metrics.py` | mae, wape, bias | BR-14 to BR-16 | 44 |
| `src/forecasting/models.py` | naive, moving_average, exponential_smoothing | | 45 to 46 |
| `src/analytics/suppliers.py` | on_time_rate, lead_time_stats | BR-17 | 51 |
| `src/ai/providers/` | Provider interface, MockProvider, ClaudeProvider | | 64 to 67 |
| `src/ai/evidence.py` | EvidenceRecord model | | 66 |
| `src/ai/claim_check.py` | find_unsupported, find_altered, find_fabricated | | 68 |
| `src/ai/tools/` | the six tools | | 71 to 75 |
| `src/ai/agent.py` | run_agent with limits | | 76 |
| `src/approval/workflow.py` | propose, approve, reject | | 78 |
| `src/approval/audit.py` | write_audit, read_history | | 79 |

## 7. Evidence record

Every number in an AI answer must have a record. The claim checker rejects answers with numbers that have no
record, numbers that differ from the record, and SKUs, branches or suppliers that do not exist.

| Field | Meaning |
|---|---|
| claim_id | Unique ID for the number in the answer |
| value | The number as returned by the tool |
| unit | Units, EUR, days, percent, ratio |
| source_tool | Tool that produced the number |
| business_rule | Rule ID from BUSINESS_RULES.md, or "lookup" for stored values |
| returned_result | Path inside the tool result, for example `rows[3].reorder_point` |
| dataset | Source table or file |
| record_keys | Keys of the record, for example sku_id SKU0042, location_id WH01 |
| run_id | Agent run that produced it |

## 8. AI agent architecture

One controlled agent. No multi-agent design.

1. Receive the user's question.
2. Decide which analysis is needed, or refuse when the data cannot support it.
3. Select one approved tool.
4. Validate arguments with Pydantic.
5. Execute the tool (timeout per call).
6. Validate the result.
7. Explain results with evidence records and assumptions.
8. Propose an action when suitable.
9. Request human approval before any consequential action.
10. Record everything in the audit log.

Limits: maximum 6 tool calls per question (configurable in `.env`), timeout per LLM call, spending limit for live
API use. Uploaded CSV content is untrusted data. Text inside data is never treated as an instruction.

## 9. Tool definitions

| Tool | Inputs | Output | Validation | Rules |
|---|---|---|---|---|
| get_inventory_summary | location_id or "ALL", as_of_date | KPI table: value, on hand, available, reserved, turnover, days of inventory, availability, accuracy | Location exists; date inside data range | BR-10, BR-11 |
| classify_inventory | scope (ALL, category, location), method (ABC, XYZ, ABC_XYZ) | Class per SKU with the values used | Method allowed; scope exists | BR-01, BR-02 |
| forecast_demand | sku_id, location_id, horizon_weeks (1 to 12), method (naive, moving_average, exp_smoothing, best) | Forecast per week plus MAE, WAPE, bias on test period | SKU exists; enough history (12 or more weeks) | BR-14 to BR-16 |
| identify_stockout_risk | horizon_days (1 to 60), top_n (1 to 50), location_id | Ranked SKUs with position, expected demand, probability | Ranges enforced | BR-03, BR-12 |
| identify_excess_inventory | cover_limit_days (30 to 365), top_n (1 to 50), location_id | Ranked SKUs with excess units and value | Ranges enforced | BR-13 |
| generate_replenishment_proposal | list of sku_id (1 to 50), location_id WH01 | Draft proposals with full calculation trail | Quantity caps; data age check; creates drafts only | BR-05 to BR-09 |

## 10. Security and human approval controls

| Control | How |
|---|---|
| No automatic orders | No code path sends orders or contacts suppliers |
| Approval mandatory | Proposals stay in state "proposed" until a person approves or rejects with a reason |
| Duplicate decisions blocked | A decided proposal cannot be decided again |
| No free SQL or Python | Tools call fixed functions only |
| Untrusted data | CSV text fields are treated as data; injection tests in TESTING_AND_EVALUATION.md |
| Secrets | API key only in `.env`, never in code or Git. `.env` is in `.gitignore` |
| Cost | Mock provider by default; spending limit; tokens and cost logged per call |
| Honest status | The app never says an action happened unless the audit log shows it |
| Synthetic data only | No real company or personal data anywhere |
