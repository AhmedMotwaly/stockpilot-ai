# Data dictionary

Every dataset in StockPilot AI. All data is synthetic, produced by the generator in `src/data/` with a fixed seed.
Formulas that use these fields: [BUSINESS_RULES.md](BUSINESS_RULES.md). Design: [PROJECT_ARCHITECTURE.md](PROJECT_ARCHITECTURE.md).

## 1. Company

10 stores (BR01 to BR10), one central warehouse (WH01), at least 500 SKUs, 6 categories, about 10 suppliers,
12 months of daily sales. Stores receive transfers from WH01. WH01 receives supplier orders.

Types: text, int, decimal (dot as decimal separator), date (YYYY-MM-DD). PK primary key, FK foreign key.

## 2. Source files

Built in two stages: version 1 by Day 13 (products, branches, suppliers, sales_history, inventory_snapshots,
inventory_movements) and version 2 by Day 19 (purchase_orders, purchase_order_lines, goods_receipts,
supplier_lead_times, planning_parameters, warehouse_activity).

### products.csv

One row per SKU. Master data.

| Field | Type | Key | Business definition and validation rule |
|---|---|---|---|
| sku_id | text | PK | SKU0001 to SKU0500 or more. Unique |
| product_name | text |  | Not empty |
| category | text |  | One of 6 categories, for example Kitchen, Electronics accessories, Home, Personal care, Stationery, Toys |
| supplier_id | text | FK suppliers | Must exist in suppliers.csv |
| unit_cost | decimal |  | EUR, above 0 |
| unit_price | decimal |  | EUR, at least unit_cost |
| pack_size | int |  | Units per supplier pack, at least 1 |
| status | text |  | active or discontinued |
| launch_date | date |  | YYYY-MM-DD, not after the data end date |

Example record:

```
SKU0042,Glass storage jar 1L,Kitchen,SUP03,2.40,4.99,12,active,2025-03-01
```

### branches.csv

Stores and the central warehouse.

| Field | Type | Key | Business definition and validation rule |
|---|---|---|---|
| branch_id | text | PK | BR01 to BR10, WH01 |
| branch_name | text |  | Not empty |
| branch_type | text |  | store or warehouse. Exactly one warehouse |
| city | text |  | Fictional or generic city name |
| size_factor | decimal |  | Demand scale, above 0. Warehouse 0 |

Example record:

```
BR03,Riverside Store,store,Northport,1.20
```

### suppliers.csv

Fictional suppliers.

| Field | Type | Key | Business definition and validation rule |
|---|---|---|---|
| supplier_id | text | PK | SUP01 onward. Unique |
| supplier_name | text |  | Fictional |
| country | text |  | Country name |
| payment_terms_days | int |  | 0 or more |
| promised_lead_time_days | int |  | Above 0 |
| min_order_value | decimal |  | EUR, 0 or more |

Example record:

```
SUP03,Northline Housewares,Poland,30,9,500.00
```

### sales_history.csv

Daily sales per store and SKU, only days with sales. 12 months.

| Field | Type | Key | Business definition and validation rule |
|---|---|---|---|
| sale_date | date | PK part | Inside the 12-month window |
| branch_id | text | PK part, FK branches | Stores only |
| sku_id | text | PK part, FK products | Must exist |
| units_sold | int |  | Above 0. Never above stock available that day |
| unit_price | decimal |  | EUR, above 0 |

Example record:

```
2026-03-14,BR03,SKU0042,3,4.99
```

### inventory_snapshots.csv

Weekly stock position per location and SKU.

| Field | Type | Key | Business definition and validation rule |
|---|---|---|---|
| snapshot_date | date | PK part | One per week |
| branch_id | text | PK part, FK branches | Including WH01 |
| sku_id | text | PK part, FK products |  |
| on_hand_units | int |  | 0 or more |
| reserved_units | int |  | 0 to on_hand_units |
| counted_units | int |  | Blank unless a count took place. Used for stock accuracy |

Example record:

```
2026-03-15,BR03,SKU0042,27,2,
```

### inventory_movements.csv

Every stock change.

| Field | Type | Key | Business definition and validation rule |
|---|---|---|---|
| movement_id | text | PK | Unique |
| movement_date | date |  |  |
| branch_id | text | FK branches |  |
| sku_id | text | FK products |  |
| movement_type | text |  | RECEIPT, SALE, TRANSFER_IN, TRANSFER_OUT, ADJUSTMENT, DAMAGE |
| quantity | int |  | Signed. Positive for RECEIPT and TRANSFER_IN, negative for SALE, TRANSFER_OUT, DAMAGE. ADJUSTMENT either sign |
| reference_id | text |  | PO or transfer number. Blank for sales |

Example record:

```
MV000123,2026-03-14,BR03,SKU0042,SALE,-3,
```

### purchase_orders.csv

Supplier orders placed by the warehouse (simulated history).

| Field | Type | Key | Business definition and validation rule |
|---|---|---|---|
| po_id | text | PK | Unique |
| supplier_id | text | FK suppliers |  |
| warehouse_id | text | FK branches | WH01 |
| order_date | date |  |  |
| expected_date | date |  | On or after order_date |
| status | text |  | OPEN, PARTIAL, RECEIVED, CANCELLED |

Example record:

```
PO2026-0310,SUP03,WH01,2026-03-02,2026-03-11,RECEIVED
```

### purchase_order_lines.csv

Lines of each purchase order.

| Field | Type | Key | Business definition and validation rule |
|---|---|---|---|
| po_id | text | PK part, FK purchase_orders |  |
| line_no | int | PK part | 1, 2, 3 |
| sku_id | text | FK products | Supplied by the order's supplier |
| ordered_qty | int |  | Above 0, multiple of pack_size |
| unit_cost | decimal |  | EUR, above 0 |

Example record:

```
PO2026-0310,1,SKU0042,240,2.40
```

### goods_receipts.csv

Receipts against order lines.

| Field | Type | Key | Business definition and validation rule |
|---|---|---|---|
| receipt_id | text | PK | Unique |
| po_id | text | FK purchase_order_lines | With line_no, must match a PO line |
| line_no | int | FK purchase_order_lines |  |
| receipt_date | date |  | On or after order_date |
| received_qty | int |  | 0 or more |
| damaged_qty | int |  | 0 to received_qty |

Example record:

```
GR000451,PO2026-0310,1,2026-03-13,240,4
```

### supplier_lead_times.csv

Lead-time statistics per supplier and SKU, derived from receipts.

| Field | Type | Key | Business definition and validation rule |
|---|---|---|---|
| supplier_id | text | PK part, FK suppliers |  |
| sku_id | text | PK part, FK products |  |
| promised_days | int |  | From suppliers.csv |
| avg_actual_days | decimal |  | Mean of receipt_date minus order_date |
| std_actual_days | decimal |  | Sample standard deviation, 0 or more |
| on_time_rate | decimal |  | 0 to 1. Rule BR-17 |
| observations | int |  | Receipts used, at least 1 |

Example record:

```
SUP03,SKU0042,9,10.4,2.1,0.75,8
```

### planning_parameters.csv

Planning settings per SKU and location.

| Field | Type | Key | Business definition and validation rule |
|---|---|---|---|
| sku_id | text | PK part, FK products |  |
| location_id | text | PK part, FK branches | WH01 for supplier orders |
| target_service_level | decimal |  | Cycle service level, 0.80 to 0.999 |
| review_period_days | int |  | At least 1 |
| min_order_qty | int |  | At least 1 |
| order_multiple | int |  | At least 1, usually pack_size |
| ordering_cost | decimal |  | EUR per order, above 0 |
| holding_cost_rate | decimal |  | Per year, 0 to 1 |

Example record:

```
SKU0042,WH01,0.95,7,24,12,25.00,0.25
```

### warehouse_activity.csv (Day 19, used by Project 2)

Daily warehouse workload for the productivity KPI.

| Field | Type | Key | Business definition and validation rule |
|---|---|---|---|
| activity_date | date | PK part |  |
| location_id | text | PK part, FK branches | WH01 |
| lines_picked | int |  | 0 or more |
| units_received | int |  | 0 or more |
| labour_hours | decimal |  | Above 0 on working days |

Example record:

```
2026-03-14,WH01,1840,2400,96.0
```


## 3. Hidden evaluation file

**true_demand.csv** holds demand before stock limits (sale_date, branch_id, sku_id, demand_units). Sales stop when stock
runs out, so recorded sales understate demand. This file is used only to measure forecast error in Project 3. The
application never reads it. It stays in `data/generated/` and is never committed. A test checks the app never opens it.

## 4. Application tables (Phases 5 and 6)

| Table | Fields | Purpose |
|---|---|---|
| proposals | proposal_id (PK), created_at, sku_id, location_id, suggested_qty, inputs_json, run_id, status (proposed, approved, rejected) | Draft replenishment proposals |
| decisions | decision_id (PK), proposal_id (FK, unique), decision (approved, rejected), reason (not empty), decided_by, decided_at | One decision per proposal |
| evidence | claim_id (PK), run_id, value, unit, source_tool, business_rule, returned_result, dataset, record_keys | Evidence for each number in AI answers |
| audit_log | event_id (PK), timestamp, run_id, user_question, tools_called, arguments_json, results_hash, response_text, provider, model, tokens_in, tokens_out, cost_eur, decision_id | Full trail of every agent run |

## 5. Relationships

```
suppliers 1--n products
suppliers 1--n purchase_orders 1--n purchase_order_lines n--1 products
purchase_order_lines 1--n goods_receipts
branches 1--n sales_history n--1 products
branches 1--n inventory_snapshots n--1 products
branches 1--n inventory_movements n--1 products
suppliers 1--n supplier_lead_times n--1 products
products 1--n planning_parameters
proposals 1--0..1 decisions
audit_log n--1 proposals (through run_id)
```

## 6. Consistency rules

1. Every foreign key exists in its parent file.
2. Dates follow the flow: order, then receipt. No receipt before its order.
3. Weekly snapshot balance equals the previous balance plus that week's movements. Differences appear only as ADJUSTMENT movements or counted_units gaps.
4. Stock never goes negative.
5. Sales never exceed stock available that day. Lost sales are recorded only in true_demand.csv.
6. Ordered quantities respect pack size and order multiples.
7. Same seed, same files.

## 7. Size

Full data: roughly 0.5 to 0.9 million sales rows. Not committed. Committed sample: 50 SKUs, 3 stores, WH01,
3 months, in `data/sample/`.
