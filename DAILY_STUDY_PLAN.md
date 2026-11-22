# Daily study plan

Master schedule for all 90 calendar days. Actual progress goes in [PROGRESS_TRACKER.md](PROGRESS_TRACKER.md).
Lessons follow [DAILY_LESSON_TEMPLATE.md](DAILY_LESSON_TEMPLATE.md). Phase goals and acceptance criteria are in
[MASTER_PROGRAMME.md](MASTER_PROGRAMME.md). Deliverable IDs (DEL-xx) are listed in MASTER_PROGRAMME.md section 4.
Business rule IDs (BR-xx) refer to [BUSINESS_RULES.md](BUSINESS_RULES.md).

**Estimated study time:** 270 minutes on every study day (78 days, 351 hours). Rest days: 0 minutes.
German and job applications: 45 minutes daily, outside this plan.

**Rule for slips:** if a day is not finished, the next day starts with the unfinished task. If you fall more than
two study days behind, apply the cut order in [RISKS_AND_RECOVERY.md](RISKS_AND_RECOVERY.md).

## Week 1 (Days 1 to 7)

### Day 1, Mon 23 Nov 2026 (Phase 1)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | SCOR overview: seven processes and where inventory control sits |
| Technical | 75 | Environment check, PowerShell basics, virtual environment, first Git commands |
| Build | 90 | Initialise Git in this folder, first commit, create the GitHub repository and push |
| Exercises and documentation | 30 | Five terminal tasks; first LEARNING_LOG entry |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** DEL-01
- **Completion criteria:** Version commands run; repository visible on GitHub; first commit pushed
- **Depends on:** Day 1 preparation checklist (README.md)

### Day 2, Tue 24 Nov 2026 (Phase 1)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Inventory terms: SKU, on hand, on order, reserved, available, lead time, service level |
| Technical | 75 | Python variables, types, conditions, loops |
| Build | 90 | Write stock_status: returns OK, REORDER or STOCKOUT |
| Exercises and documentation | 30 | Ten small Python problems with retail examples |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** src/utils/stock_status.py (practice)
- **Completion criteria:** Function returns the right status for 6 test cases
- **Depends on:** Day 1

### Day 3, Wed 25 Nov 2026 (Phase 1)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Inventory KPIs overview: turnover, days of inventory, availability, accuracy |
| Technical | 75 | Functions, lists, dictionaries, files, the csv module |
| Build | 90 | Read a 20-row CSV; compute stock value and days of cover |
| Exercises and documentation | 30 | Write three functions; compare one result with a hand calculation |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Practice script and a 20-row sample CSV
- **Completion criteria:** Printed stock value equals the hand calculation
- **Depends on:** Day 2

### Day 4, Thu 26 Nov 2026 (Phase 1)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Master data and data quality in retail |
| Technical | 75 | Exceptions, JSON, first pandas steps: read_csv, head, info |
| Build | 90 | Profiling script for missing values and duplicates |
| Exercises and documentation | 30 | Break the CSV on purpose and catch each error |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Profiling script
- **Completion criteria:** Script reports 3 planted problems
- **Depends on:** Day 3

### Day 5, Fri 27 Nov 2026 (Phase 1)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Flow from supplier to warehouse to store |
| Technical | 75 | SQL basics on SQLite: CREATE TABLE, INSERT, SELECT, WHERE, ORDER BY |
| Build | 90 | Load the sample CSV into SQLite from Python; write 8 queries |
| Exercises and documentation | 30 | Five SQL questions |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Load script and first SQL file
- **Completion criteria:** 8 queries run with the expected row counts
- **Depends on:** Day 4

### Day 6, Sat 28 Nov 2026 (Phase 1)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | What a good dataset needs: keys, dates, relationships |
| Technical | 75 | Git branches and meaningful commit messages; how to read a data dictionary |
| Build | 90 | Review DATA_DICTIONARY.md; start generator v1 for products, branches, suppliers |
| Exercises and documentation | 30 | Saturday SQL and Excel practice inside this block: 5 SQL questions and one Excel pivot on the sample CSV; baseline skills quiz |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** DEL-02 and DEL-03
- **Completion criteria:** Questions on the data dictionary logged; baseline levels written in SKILLS_MATRIX.md
- **Depends on:** Days 1 to 5

### Day 7, Sun 29 Nov 2026: rest day

No study. Optional: catch up on unfinished tasks or update PROGRESS_TRACKER.md.

## Week 2 (Days 8 to 14)

### Day 8, Mon 30 Nov 2026 (Phase 1)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Demand patterns: smooth, intermittent, seasonal |
| Technical | 75 | pytest: first tests; modules and imports |
| Build | 90 | Configuration and seeded generator for products, branches, suppliers |
| Exercises and documentation | 30 | Three tests for the generator |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Generator part 1 with tests
- **Completion criteria:** Same seed gives identical files; tests pass
- **Depends on:** Day 6

### Day 9, Tue 1 Dec 2026 (Phase 1)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Retail demand drivers: category, branch size, season, promotions |
| Technical | 75 | NumPy and pandas for random demand; reproducibility |
| Build | 90 | Sales generator: base rate, branch factor, weekly pattern |
| Exercises and documentation | 30 | Summarise the generated sales by branch and category |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Generator part 2: sales draft
- **Completion criteria:** 50 SKUs and 3 branches give plausible summaries
- **Depends on:** Day 8

### Day 10, Wed 2 Dec 2026 (Phase 1)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Seasonality, trend and intermittent demand |
| Technical | 75 | Poisson demand and noise; vectorised pandas |
| Build | 90 | Add seasonality, intermittent items, promotions; write the hidden true-demand file |
| Exercises and documentation | 30 | Chart three SKU types and describe the difference |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** sales_history.csv and true_demand.csv in data/generated
- **Completion criteria:** Seasonal items show peaks; intermittent items show many zero days
- **Depends on:** Day 9

### Day 11, Thu 3 Dec 2026 (Phase 1)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Inventory flow: receipts, sales, transfers, adjustments |
| Technical | 75 | Loops and state: simulating a daily stock balance |
| Build | 90 | Stock simulation producing movements and weekly snapshots |
| Exercises and documentation | 30 | Reconcile one SKU by hand for two weeks |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** inventory_movements.csv and inventory_snapshots.csv
- **Completion criteria:** No negative balances; snapshots reconcile with movements
- **Depends on:** Day 10

### Day 12, Fri 4 Dec 2026 (Phase 1)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Inventory accuracy and cycle counts |
| Technical | 75 | Validation functions: keys, ranges, duplicates, balances |
| Build | 90 | Validation and cleaning scripts for the six v1 files |
| Exercises and documentation | 30 | Plant 8 data problems and confirm each is caught |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** DEL-04
- **Completion criteria:** Validators catch 8 planted problems; clean data passes
- **Depends on:** Days 8 to 11

### Day 13, Sat 5 Dec 2026 (Phase 1)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Phase 1 review: how the generated company maps to the real flow |
| Technical | 75 | Integration test from generator to validators |
| Build | 90 | Run full generator v1; fix defects; tag v0.1 |
| Exercises and documentation | 30 | Saturday SQL and Excel practice inside this block: 6 SQL questions on the generated data; one Excel pivot |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** DEL-05
- **Completion criteria:** Phase 1 acceptance criteria in MASTER_PROGRAMME.md met
- **Depends on:** Days 8 to 12

### Day 14, Sun 6 Dec 2026: rest day

No study. Optional: catch up on unfinished tasks or update PROGRESS_TRACKER.md.

## Week 3 (Days 15 to 21)

### Day 15, Mon 7 Dec 2026 (Phase 2)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Inventory KPI definitions: turnover and days of inventory |
| Technical | 75 | pandas selection and filtering |
| Build | 90 | Database loader: generated CSV files into SQLite |
| Exercises and documentation | 30 | Check row counts table by table |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Loader script; database file (ignored by Git)
- **Completion criteria:** Row counts match the CSV files for six tables
- **Depends on:** Day 13

### Day 16, Tue 8 Dec 2026 (Phase 2)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Availability and stock accuracy definitions |
| Technical | 75 | pandas groupby and merge |
| Build | 90 | First KPI calculations in pandas: stock value by branch, availability |
| Exercises and documentation | 30 | Check one branch manually with SQL |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** KPI draft module
- **Completion criteria:** KPIs match a manual SQL check for one branch
- **Depends on:** Day 15

### Day 17, Wed 9 Dec 2026 (Phase 2)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Branch comparison logic |
| Technical | 75 | SQL GROUP BY, HAVING and aggregates |
| Build | 90 | SQL queries 1 to 5 in database/queries/ |
| Exercises and documentation | 30 | Cross-check each result with pandas |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Queries 1 to 5
- **Completion criteria:** Each result matches pandas
- **Depends on:** Day 16

### Day 18, Thu 10 Dec 2026 (Phase 2)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Procure to pay: purchase order, receipt, invoice |
| Technical | 75 | SQL JOINs |
| Build | 90 | Generator v2 part 1: purchase_orders and purchase_order_lines |
| Exercises and documentation | 30 | Three JOIN questions on the new tables |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Generator v2 part 1
- **Completion criteria:** All PO lines reference valid SKUs and suppliers
- **Depends on:** Day 13

### Day 19, Fri 11 Dec 2026 (Phase 2)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Supplier lead time and on-time delivery |
| Technical | 75 | SQL CASE and subqueries |
| Build | 90 | Generator v2 part 2: goods_receipts, supplier_lead_times, planning_parameters, warehouse_activity |
| Exercises and documentation | 30 | Write a CASE query that labels late receipts |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** DEL-06
- **Completion criteria:** Receipts follow order dates; validators pass on all files
- **Depends on:** Day 18

### Day 20, Sat 12 Dec 2026 (Phase 2)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Data quality in an inventory analytics team |
| Technical | 75 | CTEs and window functions |
| Build | 90 | Data-quality checks (8) and report |
| Exercises and documentation | 30 | Saturday SQL and Excel practice inside this block: window-function questions; Excel lookup and pivot on supplier data |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** DEL-07
- **Completion criteria:** 8 checks run; the report lists the planted issues
- **Depends on:** Days 13 to 19

### Day 21, Sun 13 Dec 2026: rest day

No study. Optional: catch up on unfinished tasks or update PROGRESS_TRACKER.md.

## Week 4 (Days 22 to 28)

### Day 22, Mon 14 Dec 2026 (Phase 2)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | When Excel is the right tool and when it is not |
| Technical | 75 | Excel Power Query: import, clean, merge |
| Build | 90 | Load the generated CSV files in Power Query |
| Exercises and documentation | 30 | Document each Power Query step |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Power Query steps documented in dashboard/
- **Completion criteria:** Dimension and fact tables load without errors
- **Depends on:** Day 19

### Day 23, Tue 15 Dec 2026 (Phase 2)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | KPI design: definition, owner, target |
| Technical | 75 | Power BI data model: star schema and relationships |
| Build | 90 | Build the data model |
| Exercises and documentation | 30 | Draw the model and explain each relationship |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Model diagram in dashboard/
- **Completion criteria:** Relationships use the correct keys and direction
- **Depends on:** Day 22

### Day 24, Wed 16 Dec 2026 (Phase 2)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Turnover and days of inventory in business use |
| Technical | 75 | DAX measure basics |
| Build | 90 | Measures: inventory value, turnover, days of inventory; SQL queries 6 to 10 |
| Exercises and documentation | 30 | Compare each measure with the Python KPI |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Measures v1 and queries 6 to 10
- **Completion criteria:** Measures match the Python KPIs within 0.5 percent
- **Depends on:** Day 23

### Day 25, Thu 17 Dec 2026 (Phase 2)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Availability, accuracy and supplier delivery KPIs |
| Technical | 75 | DAX filter context and CALCULATE |
| Build | 90 | Measures: availability, accuracy, on-time delivery, lead time; SQL queries 11 to 15 |
| Exercises and documentation | 30 | Write one note per measure |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** DEL-08
- **Completion criteria:** 15 saved queries; measures match SQL results
- **Depends on:** Day 24

### Day 26, Fri 18 Dec 2026 (Phase 2)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Dashboard design for managers |
| Technical | 75 | Power BI visuals, slicers, layout |
| Build | 90 | Dashboard pages: overview and branch performance |
| Exercises and documentation | 30 | Remove one chart that adds nothing and record why |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Dashboard draft
- **Completion criteria:** 8 KPIs visible; slicers work
- **Depends on:** Day 25

### Day 27, Sat 19 Dec 2026 (Phase 2)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Business interpretation of branch results |
| Technical | 75 | Documenting a data model and its measures |
| Build | 90 | Supplier and inventory health pages; branch performance report; tag v0.2 |
| Exercises and documentation | 30 | Saturday SQL and Excel practice inside this block: reproduce 3 dashboard numbers in Excel |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** DEL-09 and DEL-10
- **Completion criteria:** Phase 2 acceptance criteria met
- **Depends on:** Days 22 to 26

### Day 28, Sun 20 Dec 2026: rest day

No study. Optional: catch up on unfinished tasks or update PROGRESS_TRACKER.md.

## Week 5 (Days 29 to 35)

### Day 29, Mon 21 Dec 2026 (Phase 3)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | ABC analysis: purpose and method |
| Technical | 75 | pandas sorting and cumulative sums |
| Build | 90 | ABC function with tests |
| Exercises and documentation | 30 | Solve the BR-01 example by hand first |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** ABC module and tests
- **Completion criteria:** Tests pass for the BR-01 example
- **Depends on:** Day 27

### Day 30, Tue 22 Dec 2026 (Phase 3)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Demand variability and XYZ |
| Technical | 75 | Standard deviation and coefficient of variation in pandas |
| Build | 90 | XYZ function with tests |
| Exercises and documentation | 30 | Solve the BR-02 example by hand first |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** XYZ module and tests
- **Completion criteria:** Tests pass for the BR-02 example
- **Depends on:** Day 29

### Day 31, Wed 23 Dec 2026 (Phase 3)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | ABC/XYZ matrix and policy by segment |
| Technical | 75 | pytest parametrize and fixtures |
| Build | 90 | Matrix and business explanation text per segment |
| Exercises and documentation | 30 | Write one policy sentence per segment |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** DEL-11
- **Completion criteria:** Matrix totals equal the SKU count
- **Depends on:** Days 29 and 30

### Day 32, Thu 24 Dec 2026 (Phase 3)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Lead time and lead-time demand |
| Technical | 75 | Type hints and docstrings |
| Build | 90 | Average demand, variability and lead-time demand functions |
| Exercises and documentation | 30 | Hand-check BR-03 and BR-04 |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Demand statistics module
- **Completion criteria:** BR-03 and BR-04 examples reproduced
- **Depends on:** Day 31

### Day 33, Fri 25 Dec 2026 (Phase 3)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Service level: cycle service level versus fill rate |
| Technical | 75 | Normal distribution with statistics.NormalDist |
| Build | 90 | Safety stock functions for fixed and variable lead time |
| Exercises and documentation | 30 | Hand-check BR-05 and BR-06 |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Safety stock module
- **Completion criteria:** Both safety-stock examples reproduced
- **Depends on:** Day 32

### Day 34, Sat 26 Dec 2026 (Phase 3)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Reorder point and review policies |
| Technical | 75 | pytest numeric tolerance (pytest.approx) |
| Build | 90 | Reorder point and order-up-to level |
| Exercises and documentation | 30 | Saturday SQL and Excel practice inside this block: replicate the reorder point for 3 SKUs in Excel and compare |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Reorder module
- **Completion criteria:** BR-07 reproduced; the Excel check matches
- **Depends on:** Day 33

### Day 35, Sun 27 Dec 2026: rest day

No study. Optional: catch up on unfinished tasks or update PROGRESS_TRACKER.md.

## Week 6 (Days 36 to 42)

### Day 36, Mon 28 Dec 2026 (Phase 3)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | EOQ: assumptions and limits |
| Technical | 75 | Constants and configuration |
| Build | 90 | EOQ function and planning-parameter loader |
| Exercises and documentation | 30 | Hand-check BR-08 |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** EOQ module
- **Completion criteria:** BR-08 example reproduced
- **Depends on:** Day 34

### Day 37, Tue 29 Dec 2026 (Phase 3)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Inventory position, minimum order quantity, order multiples |
| Technical | 75 | pandas apply and vectorised logic |
| Build | 90 | Replenishment quantity rule and proposals table |
| Exercises and documentation | 30 | Check 3 proposals against BR-09 |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Replenishment module
- **Completion criteria:** Proposals respect minimum quantity and multiples
- **Depends on:** Day 36

### Day 38, Wed 30 Dec 2026 (Phase 3)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Stockout risk |
| Technical | 75 | Probability with the normal approximation |
| Build | 90 | Stockout probability and risk levels |
| Exercises and documentation | 30 | Hand-check BR-12 |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Stockout risk module
- **Completion criteria:** BR-12 example reproduced
- **Depends on:** Day 37

### Day 39, Thu 31 Dec 2026 (Phase 3)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Excess, slow-moving and obsolete stock |
| Technical | 75 | Conditional logic in pandas |
| Build | 90 | Excess and slow-moving detection |
| Exercises and documentation | 30 | Confirm seeded excess items are found |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Excess module
- **Completion criteria:** Seeded excess items detected
- **Depends on:** Day 38

### Day 40, Fri 1 Jan 2027 (Phase 3)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Linking KPIs to planning decisions |
| Technical | 75 | Integration tests |
| Build | 90 | Planning pipeline: dataset to proposals file, no AI |
| Exercises and documentation | 30 | Write a one-page explanation of the pipeline |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** DEL-12
- **Completion criteria:** Pipeline runs end to end on generated data
- **Depends on:** Days 29 to 39

### Day 41, Sat 2 Jan 2027 (Phase 3)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Phase 3 review: what the engine says and does not say |
| Technical | 75 | Test coverage review |
| Build | 90 | Finish tests and hand-calculation records; tag v0.3 |
| Exercises and documentation | 30 | Saturday SQL and Excel practice inside this block: Excel cross-check of two replenishment proposals |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** DEL-13 and DEL-14
- **Completion criteria:** 30 or more tests pass; 5 hand checks recorded
- **Depends on:** Day 40

### Day 42, Sun 3 Jan 2027: rest day

No study. Optional: catch up on unfinished tasks or update PROGRESS_TRACKER.md.

## Week 7 (Days 43 to 49)

### Day 43, Mon 4 Jan 2027 (Phase 4)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Forecasting basics and demand patterns |
| Technical | 75 | Time series in pandas: resample and rolling |
| Build | 90 | Weekly aggregation and chronological train/test split |
| Exercises and documentation | 30 | Prove with a test that train and test never overlap |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Data preparation module
- **Completion criteria:** Split keeps time order
- **Depends on:** Day 41

### Day 44, Tue 5 Jan 2027 (Phase 4)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Forecast accuracy: MAE, WAPE, bias |
| Technical | 75 | Metric functions with tests |
| Build | 90 | Metrics module |
| Exercises and documentation | 30 | Hand-check BR-14 to BR-16 |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Metrics module
- **Completion criteria:** BR-14 to BR-16 reproduced
- **Depends on:** Day 43

### Day 45, Wed 6 Jan 2027 (Phase 4)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Moving averages and the naive baseline |
| Technical | 75 | Rolling windows without leakage |
| Build | 90 | Naive and moving-average forecasts |
| Exercises and documentation | 30 | Write a leakage test |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Simple forecasts module
- **Completion criteria:** Forecasts use only past data; leakage test passes
- **Depends on:** Day 44

### Day 46, Thu 7 Jan 2027 (Phase 4)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Exponential smoothing |
| Technical | 75 | Recursive calculation; parameter search on training data only |
| Build | 90 | Exponential smoothing with alpha search |
| Exercises and documentation | 30 | Hand-calculate a 4-period example |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Smoothing module
- **Completion criteria:** Hand example matches
- **Depends on:** Day 45

### Day 47, Fri 8 Jan 2027 (Phase 4)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Seasonality exploration |
| Technical | 75 | Grouping by week and month; Plotly charts |
| Build | 90 | Seasonality charts for 5 SKUs |
| Exercises and documentation | 30 | Classify 5 SKUs as seasonal or flat and explain |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Seasonality notebook (Project 3)
- **Completion criteria:** Charts separate seasonal from flat items
- **Depends on:** Day 46

### Day 48, Sat 9 Jan 2027 (Phase 4)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Choosing a forecast method by demand pattern |
| Technical | 75 | Comparison tables |
| Build | 90 | Compare methods for 20 to 30 SKUs; save results |
| Exercises and documentation | 30 | Saturday SQL and Excel practice inside this block: recalculate WAPE for one SKU in Excel |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** DEL-15
- **Completion criteria:** Module tested; comparison runs for 20 to 30 SKUs
- **Depends on:** Days 43 to 47

### Day 49, Sun 10 Jan 2027: rest day

No study. Optional: catch up on unfinished tasks or update PROGRESS_TRACKER.md.

## Week 8 (Days 50 to 56)

### Day 50, Mon 11 Jan 2027 (Phase 4)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Business impact of forecast error |
| Technical | 75 | Scenario calculation: effect of bias on stock and service |
| Build | 90 | Forecast comparison report |
| Exercises and documentation | 30 | Explain one result to a non-technical manager in 5 sentences |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** DEL-16
- **Completion criteria:** Report names the best method per demand pattern with numbers
- **Depends on:** Day 48

### Day 51, Tue 12 Jan 2027 (Phase 4)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Supplier lead-time performance |
| Technical | 75 | Date arithmetic in pandas |
| Build | 90 | Lead-time and on-time metrics |
| Exercises and documentation | 30 | Hand-check BR-17 |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Supplier metrics module
- **Completion criteria:** BR-17 example reproduced
- **Depends on:** Day 19

### Day 52, Wed 13 Jan 2027 (Phase 4)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Root-cause analysis: 5 Whys and Pareto |
| Technical | 75 | Pareto chart with Plotly |
| Build | 90 | Supplier performance analysis and root-cause note |
| Exercises and documentation | 30 | Run a 5 Whys on the worst supplier |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** DEL-17
- **Completion criteria:** Analysis names the late suppliers with evidence
- **Depends on:** Day 51

### Day 53, Thu 14 Jan 2027 (Phase 4)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Exception management: what deserves attention |
| Technical | 75 | Rule engines in pandas |
| Build | 90 | Exception rules part 1: stockout, excess, slow moving |
| Exercises and documentation | 30 | Rank exceptions by value |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Exceptions module part 1
- **Completion criteria:** Seeded exceptions flagged
- **Depends on:** Days 40 and 52

### Day 54, Fri 15 Jan 2027 (Phase 4)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Unusual demand and high-value exceptions |
| Technical | 75 | Z-score and interquartile range |
| Build | 90 | Exception rules part 2: lead time, unusual demand, data quality, high value |
| Exercises and documentation | 30 | Evidence checkpoint: mark every deliverable Complete, Partial or Not started |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Evidence checkpoint (see MASTER_PROGRAMME.md section 9)
- **Completion criteria:** PROGRESS_TRACKER.md shows the true status of DEL-01 to DEL-19
- **Depends on:** Day 53

### Day 55, Sat 16 Jan 2027 (Phase 4)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Reading an exception report as a planner |
| Technical | 75 | Report generation: CSV and markdown |
| Build | 90 | Inventory exception report; finish the Project 3 draft; tag v0.4 |
| Exercises and documentation | 30 | Saturday SQL and Excel practice inside this block: SQL and Excel check of three exception rows |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** DEL-18 and DEL-19
- **Completion criteria:** Phase 4 acceptance criteria met
- **Depends on:** Days 50 to 54

### Day 56, Sun 17 Jan 2027: rest day

No study. Optional: catch up on unfinished tasks or update PROGRESS_TRACKER.md.

## Week 9 (Days 57 to 63)

### Day 57, Mon 18 Jan 2027 (Phase 5)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Master data, ERP and MRP basics |
| Technical | 75 | Streamlit: pages, widgets, layout |
| Build | 90 | App skeleton with navigation |
| Exercises and documentation | 30 | Sketch the pages on paper first |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** app/ skeleton
- **Completion criteria:** streamlit run opens a page with navigation
- **Depends on:** Day 55

### Day 58, Tue 19 Jan 2027 (Phase 5)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | How planners receive data: files and interfaces |
| Technical | 75 | Streamlit file upload and session state |
| Build | 90 | CSV upload page using the validators |
| Exercises and documentation | 30 | Upload three broken files and read the messages |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Upload page
- **Completion criteria:** Bad files show clear error messages
- **Depends on:** Day 57

### Day 59, Wed 20 Jan 2027 (Phase 5)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Dashboard design for planners |
| Technical | 75 | Plotly in Streamlit |
| Build | 90 | Inventory dashboard page |
| Exercises and documentation | 30 | Compare 3 KPIs with Power BI |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Dashboard page
- **Completion criteria:** KPIs match Python and Power BI values
- **Depends on:** Day 58

### Day 60, Thu 21 Jan 2027 (Phase 5)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Planning review meeting inputs |
| Technical | 75 | SQLite access layer |
| Build | 90 | Load uploaded data into the database |
| Exercises and documentation | 30 | Run the app from a fresh clone |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** DEL-20
- **Completion criteria:** App runs on a clean clone
- **Depends on:** Days 57 to 59

### Day 61, Fri 22 Jan 2027 (Phase 5)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Replenishment review workflow |
| Technical | 75 | Caching and performance |
| Build | 90 | Forecasting and planning pages |
| Exercises and documentation | 30 | Check that every proposal row shows its calculation inputs |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** DEL-21
- **Completion criteria:** Proposals table shows calculation columns
- **Depends on:** Day 60

### Day 62, Sat 23 Jan 2027 (Phase 5)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Exception review routine |
| Technical | 75 | Error handling and logging |
| Build | 90 | Exceptions page and logging configuration |
| Exercises and documentation | 30 | Saturday SQL and Excel practice inside this block: SQL on proposal data; Excel check of 3 KPIs |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Exceptions page
- **Completion criteria:** Errors are logged, not shown as raw tracebacks
- **Depends on:** Day 61

### Day 63, Sun 24 Jan 2027: rest day

No study. Optional: catch up on unfinished tasks or update PROGRESS_TRACKER.md.

## Week 10 (Days 64 to 70)

### Day 64, Mon 25 Jan 2027 (Phase 5)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | What a weekly supply briefing contains |
| Technical | 75 | LLM basics, APIs, authentication, environment variables |
| Build | 90 | Provider interface and .env handling |
| Exercises and documentation | 30 | Explain where the API key lives and why |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Provider interface
- **Completion criteria:** Interface has mock and Claude slots; no key in code
- **Depends on:** Day 62

### Day 65, Tue 26 Jan 2027 (Phase 5)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Briefing structure: findings, causes, actions |
| Technical | 75 | Pydantic models and structured outputs |
| Build | 90 | Mock provider returning a structured briefing |
| Exercises and documentation | 30 | Run the app with no API key |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Mock provider
- **Completion criteria:** App works with no API key
- **Depends on:** Day 64

### Day 66, Wed 27 Jan 2027 (Phase 5)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Evidence-based reporting |
| Technical | 75 | Designing evidence records |
| Build | 90 | Evidence record model (see PROJECT_ARCHITECTURE.md section 7) |
| Exercises and documentation | 30 | Link three briefing numbers to their evidence records |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Evidence module
- **Completion criteria:** Each number in a briefing links to an evidence record
- **Depends on:** Day 65

### Day 67, Thu 28 Jan 2027 (Phase 5)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | What managers ask about stock |
| Technical | 75 | Prompt design; cost, timeout and error handling |
| Build | 90 | Optional Claude provider with limits |
| Exercises and documentation | 30 | Simulate an API failure and read the message |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** DEL-22
- **Completion criteria:** Claude provider fails safely without a key; timeout works
- **Depends on:** Day 66

### Day 68, Fri 29 Jan 2027 (Phase 5)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Briefing quality criteria |
| Technical | 75 | Claim checking: unsupported, altered and fabricated numbers |
| Build | 90 | Claim checker and tests |
| Exercises and documentation | 30 | Write one test per claim type |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Claim checker
- **Completion criteria:** Checker flags 3 planted bad claims of each type
- **Depends on:** Day 66

### Day 69, Sat 30 Jan 2027 (Phase 5)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Phase 5 review: what a briefing may and may not say |
| Technical | 75 | Integration test |
| Build | 90 | AI briefing page; Phase 5 check; tag v0.5 |
| Exercises and documentation | 30 | Saturday SQL and Excel practice inside this block: SQL and Excel questions on evidence records |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** DEL-23
- **Completion criteria:** Phase 5 acceptance criteria met
- **Depends on:** Days 64 to 68

### Day 70, Sun 31 Jan 2027: rest day

No study. Optional: catch up on unfinished tasks or update PROGRESS_TRACKER.md.

## Week 11 (Days 71 to 77)

### Day 71, Mon 1 Feb 2027 (Phase 6)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | From question to decision: the replenishment flow |
| Technical | 75 | Tool calling and JSON schemas |
| Build | 90 | Pydantic input and output models for the six tools |
| Exercises and documentation | 30 | Feed invalid arguments and read the errors |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Tool models
- **Completion criteria:** Models reject invalid arguments
- **Depends on:** Day 69

### Day 72, Tue 2 Feb 2027 (Phase 6)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | What a manager needs from an inventory summary |
| Technical | 75 | Wrapping Python functions as tools |
| Build | 90 | Tools get_inventory_summary and classify_inventory |
| Exercises and documentation | 30 | Compare tool output with direct function output |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Two tools with tests
- **Completion criteria:** Tool results equal direct function results
- **Depends on:** Day 71

### Day 73, Wed 3 Feb 2027 (Phase 6)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Using forecasts in decisions |
| Technical | 75 | Argument validation and limits |
| Build | 90 | Tool forecast_demand |
| Exercises and documentation | 30 | Try a horizon above the limit |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Forecast tool with tests
- **Completion criteria:** Horizon limits enforced
- **Depends on:** Day 72

### Day 74, Thu 4 Feb 2027 (Phase 6)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Risk and excess from the planner's view |
| Technical | 75 | Ranking and top-N logic |
| Build | 90 | Tools identify_stockout_risk and identify_excess_inventory |
| Exercises and documentation | 30 | Check the top 5 against the planning engine |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Two tools with tests
- **Completion criteria:** Top-N results match the planning engine
- **Depends on:** Day 73

### Day 75, Fri 5 Feb 2027 (Phase 6)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Reviewing a replenishment proposal |
| Technical | 75 | Caps, rounding and validation |
| Build | 90 | Tool generate_replenishment_proposal with quantity caps |
| Exercises and documentation | 30 | Try to break the cap |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** DEL-24
- **Completion criteria:** All six tools tested; proposals never exceed caps
- **Depends on:** Days 71 to 74

### Day 76, Sat 6 Feb 2027 (Phase 6)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Controls in replenishment |
| Technical | 75 | Agent loop, step limits, timeouts |
| Build | 90 | Agent controller with the mock provider |
| Exercises and documentation | 30 | Saturday SQL and Excel practice inside this block: SQL on tool-call logs; Excel summary of tool usage |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** DEL-25
- **Completion criteria:** Agent stops at the tool limit; refuses unsupported questions
- **Depends on:** Day 75

### Day 77, Sun 7 Feb 2027: rest day

No study. Optional: catch up on unfinished tasks or update PROGRESS_TRACKER.md.

## Week 12 (Days 78 to 84)

### Day 78, Mon 8 Feb 2027 (Phase 6)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Approval controls in purchasing |
| Technical | 75 | State machines: proposed, approved, rejected |
| Build | 90 | Proposals with approve and reject, reason and timestamp |
| Exercises and documentation | 30 | Try to decide the same proposal twice |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Approval workflow
- **Completion criteria:** Duplicate decisions are rejected
- **Depends on:** Day 76

### Day 79, Tue 9 Feb 2027 (Phase 6)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Audit trail basics |
| Technical | 75 | Audit schema and logging |
| Build | 90 | Audit log and history page |
| Exercises and documentation | 30 | Trace one decision back to its tool results |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** DEL-26
- **Completion criteria:** Every decision has a complete audit record
- **Depends on:** Day 78

### Day 80, Wed 10 Feb 2027 (Phase 6)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Risk and resilience in planning |
| Technical | 75 | Evaluation design |
| Build | 90 | Evaluation cases EV-01 to EV-20 in evals/ |
| Exercises and documentation | 30 | Write the expected behaviour for each case |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Evaluation cases 1 to 20
- **Completion criteria:** Each case has an expected tool and expected behaviour
- **Depends on:** Day 79

### Day 81, Thu 11 Feb 2027 (Phase 6)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Scenario thinking: late supplier, demand spike |
| Technical | 75 | Prompt injection and untrusted data |
| Build | 90 | Hostile CSV fixtures and security tests |
| Exercises and documentation | 30 | Plant two hostile fields and confirm no action follows |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** DEL-27
- **Completion criteria:** Injection tests pass; secrets scan is clean
- **Depends on:** Day 80

### Day 82, Fri 12 Feb 2027 (Phase 6)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | KPIs for judging AI support |
| Technical | 75 | Evaluation runner |
| Build | 90 | Evaluation cases EV-21 to EV-40 and the runner |
| Exercises and documentation | 30 | Run all 40 cases in mock mode |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** Evaluation cases 21 to 40 and runner
- **Completion criteria:** 40 cases run with the mock provider
- **Depends on:** Day 81

### Day 83, Sat 13 Feb 2027 (Phase 6)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Reading evaluation results honestly |
| Technical | 75 | Fixing failures test-first |
| Build | 90 | Run the evaluation, record results, fix; tag v0.6 |
| Exercises and documentation | 30 | Saturday SQL and Excel practice inside this block: SQL and Excel summary of evaluation results |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** DEL-28
- **Completion criteria:** Phase 6 acceptance criteria met
- **Depends on:** Days 76 to 82

### Day 84, Sun 14 Feb 2027: rest day

No study. Optional: catch up on unfinished tasks or update PROGRESS_TRACKER.md.

## Week 13 (Days 85 to 90)

### Day 85, Mon 15 Feb 2027 (Phase 7)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Telling the supply-chain story with SCOR |
| Technical | 75 | Architecture diagrams |
| Build | 90 | Final README and architecture diagram |
| Exercises and documentation | 30 | Read the README as a stranger and fix gaps |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** DEL-29 part 1
- **Completion criteria:** README matches the code as it exists
- **Depends on:** Day 83

### Day 86, Tue 16 Feb 2027 (Phase 7)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Formulas and data in documentation |
| Technical | 75 | Checking documentation against code |
| Build | 90 | Final data dictionary and formula checks |
| Exercises and documentation | 30 | Spot-check 5 formulas against the code |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** DEL-29
- **Completion criteria:** Every formula and field in the docs matches the code
- **Depends on:** Day 85

### Day 87, Wed 17 Feb 2027 (Phase 7)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Evidence and limits in reporting |
| Technical | 75 | Writing a test report |
| Build | 90 | Fill TESTING_AND_EVALUATION.md results with real numbers |
| Exercises and documentation | 30 | List known failures honestly |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** DEL-30
- **Completion criteria:** Report states pass counts and known failures
- **Depends on:** Day 86

### Day 88, Thu 18 Feb 2027 (Phase 7)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Presenting KPIs to managers |
| Technical | 75 | Screenshots and dashboard documentation |
| Build | 90 | Power BI documentation and screenshots; finish Project 3 |
| Exercises and documentation | 30 | Explain each DAX measure in one sentence |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** DEL-31
- **Completion criteria:** Each DAX measure explained; Project 3 final
- **Depends on:** Day 87

### Day 89, Fri 19 Feb 2027 (Phase 7)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Explaining a project in business terms |
| Technical | 75 | Screen recording and demo script |
| Build | 90 | Record the 3 to 5 minute demo video |
| Exercises and documentation | 30 | Rehearse the demo twice |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** DEL-32
- **Completion criteria:** Video shows upload, briefing, agent, approval and audit
- **Depends on:** Day 88

### Day 90, Sat 20 Feb 2027 (Phase 7)

| Block | Minutes | Task |
|---|---|---|
| Supply chain | 45 | Interview preparation: inventory, analytics, AI |
| Technical | 75 | CV and LinkedIn writing |
| Build | 90 | CV text, LinkedIn text, interview presentation; tag v1.0 |
| Exercises and documentation | 30 | Saturday SQL and Excel practice inside this block: mock SQL and Excel interview task |
| Review and GitHub | 30 | Run tests, commit, push, update PROGRESS_TRACKER.md |

- **Deliverable:** DEL-33
- **Completion criteria:** Final portfolio checklist complete
- **Depends on:** Days 85 to 89
