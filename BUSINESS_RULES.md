# Business rules

Formulas, assumptions and worked examples. Code must reproduce each example in a pytest test before the rule is
used anywhere else. The AI layer never computes these values. Field names: [DATA_DICTIONARY.md](DATA_DICTIONARY.md).

Notation: d average daily demand, sigma_d standard deviation of daily demand, L lead time in days,
sigma_L standard deviation of lead time, z service factor, D annual demand.

## BR-01 ABC classification

**Purpose:** focus attention on the SKUs that carry most of the value.

**Formula:** annual consumption value = units sold in 12 months x unit_cost. Sort descending. Cumulative share =
running total / grand total. Class A if cumulative share is at most 0.80, B if at most 0.95, otherwise C.

**Example:** values 5,000; 3,000; 1,000; 600; 400 (total 10,000). Cumulative shares 0.50, 0.80, 0.90, 0.96, 1.00.
Classes A, A, B, C, C.

**Assumptions and limits:** thresholds are a convention (stored in configuration). ABC ignores demand stability; use with XYZ.

**Python:** `src/inventory/classification.py` abc_class (Day 29).

## BR-02 XYZ classification

**Purpose:** separate stable demand from erratic demand.

**Formula:** coefficient of variation CV = sample standard deviation / mean of weekly demand. X if CV below 0.5,
Y if 0.5 to 1.0, Z above 1.0. SKUs with mean 0 are class Z and flagged.

**Example:** weekly demand 10, 12, 8, 11, 9, 10. Mean 10. Sample standard deviation 1.414.
CV 0.141. Class X.

**Assumptions and limits:** needs at least 12 weeks of history. Intermittent items show high CV by nature.

**Python:** `src/inventory/classification.py` xyz_class (Day 30).

## BR-03 Average demand and variability

**Formula:** d = total units / number of days in the period, including zero-sales days.
sigma_d = sample standard deviation of daily units, including zeros.

**Limit:** recorded sales understate demand during stockouts.

**Python:** `src/inventory/demand_stats.py` (Day 32).

## BR-04 Lead-time demand

**Formula:** LTD = d x L.

**Example:** d = 20 units per day, L = 9 days. LTD = 180 units.

**Python:** `src/inventory/demand_stats.py` lead_time_demand (Day 32).

## BR-05 Safety stock, fixed lead time

**Purpose:** buffer against demand variation during the lead time.

**Formula:** SS = z x sigma_d x sqrt(L). z = inverse normal of the cycle service level.

**Example:** service level 0.95 gives z = 1.6449. sigma_d = 6, L = 9. SS = 1.6449 x 6 x 3 =
29.61, rounded up to 30 units.

**Assumptions:** demand per day is independent and roughly normal; lead time is constant.

**Python:** `src/inventory/safety_stock.py` safety_stock_fixed_lt (Day 33).

## BR-06 Safety stock, variable lead time

**Formula:** SS = z x sqrt(L x sigma_d^2 + d^2 x sigma_L^2).

**Example:** z = 1.6449, L = 9, sigma_d = 6, d = 20, sigma_L = 2.
SS = 1.6449 x sqrt(324 + 1600) = 72.15, rounded up to 73 units.

**Assumptions:** demand and lead time are independent. Use this rule when supplier lead times vary (supplier_lead_times.std_actual_days above 0).

**Python:** `src/inventory/safety_stock.py` safety_stock_variable_lt (Day 33).

### Cycle service level versus fill rate

Cycle service level is the probability of no stockout during one replenishment cycle. Fill rate is the share of
demand served from stock. A 95 percent cycle service level usually gives a fill rate above 95 percent, because a
stockout often affects only part of a cycle's demand. StockPilot sets safety stock by cycle service level and
reports fill rate separately where data allows. Never treat the two as the same number.

## BR-07 Reorder point

**Formula:** ROP = LTD + SS. Order when inventory position (on hand + on order - reserved) is at or below ROP.

**Example:** LTD 180 + SS 29.61 = 209.61, rounded up to 210 units.

**Python:** `src/inventory/reorder.py` reorder_point (Day 34).

## BR-08 Economic order quantity

**Formula:** EOQ = sqrt(2 x D x S / H). S ordering cost per order, H = holding_cost_rate x unit_cost per unit per year.

**Example:** D = 7,300, S = 25 EUR, H = 0.25 x 4.00 = 1.00 EUR. EOQ = sqrt(365,000) = 604.15, about 604 units.

**Assumptions:** steady demand, fixed costs, no quantity discounts. Treat EOQ as a guide, then apply BR-09.

**Python:** `src/inventory/eoq.py` (Day 36).

## BR-09 Suggested replenishment quantity

**Rule:** if inventory position is at or below ROP, order up to target stock = ROP + max(EOQ, d x review_period_days).
Quantity = target stock - inventory position, then raised to min_order_qty and rounded up to order_multiple.
Cap: never more than 120 days of average demand. Over the cap, the proposal is flagged, not created.

**Example:** position 180, ROP 210, EOQ 604, d = 20, review 7 days, min order 24, multiple 12.
Target = 210 + 604 = 814. Quantity = 634, rounded up to 636. Cap = 2,400. Proposal 636 units.

**Python:** `src/inventory/replenishment.py` (Day 37).

## BR-10 Inventory turnover

**Formula:** turnover = cost of goods sold in the period / average inventory value at cost.

**Example:** COGS 120,000 EUR, average inventory value 30,000 EUR. Turnover = 4.

**Python:** `src/analytics/kpis.py` turnover (Day 16 to 24).

## BR-11 Days of inventory

**Formula:** days of inventory = 365 / turnover (annual), or average inventory value / average daily COGS.

**Example:** turnover 4. Days of inventory = 91.25.

## BR-12 Stockout risk

**Formula:** over horizon H days, expected demand mu = d x H, standard deviation sigma_H = sigma_d x sqrt(H).
Probability of stockout = P(demand above inventory position) = 1 - Phi((position - mu) / sigma_H).
Risk levels: high 0.5 or more, medium 0.2 to below 0.5, low below 0.2.

**Example:** position 250, d = 20, sigma_d = 6, H = 14. mu = 280, sigma_H = 22.45,
z = -1.336. Probability 0.909 (about 91 percent). High risk.

**Assumption:** ignores receipts due inside the horizon unless they are in "on order".

**Python:** `src/inventory/risk.py` stockout_probability (Day 38).

## BR-13 Excess and slow-moving inventory

**Rule:** days of cover = on hand / d. Excess if days of cover is above the cover limit (default 120 days):
excess units = on hand - cover limit x d; excess value = excess units x unit_cost.
Slow-moving: no sale in the last 90 days with on hand above 0. Obsolete candidate: no sale in 180 days or status discontinued.

**Example:** on hand 900, d = 5, limit 120. Cover 180 days. Excess 300 units. At 2.40 EUR, excess value 720 EUR.

**Python:** `src/inventory/risk.py` excess_units (Day 39).

## BR-14 MAE, BR-15 WAPE, BR-16 Forecast bias

**Formulas:** MAE = mean of |forecast - actual|. WAPE = sum of |forecast - actual| / sum of actual.
Bias = (sum of forecast - sum of actual) / sum of actual. Negative bias means under-forecasting.

**Example:** actual 100, 110, 95, 105 (sum 410). Forecast 110, 100, 100, 95 (sum 405).
Absolute errors 10, 10, 5, 10 (sum 35). MAE = 8.75. WAPE = 0.0854. Bias = -0.0122.

**Assumptions:** WAPE is preferred over MAPE because MAPE breaks on zero-demand weeks. Always compare with the naive forecast.

**Python:** `src/forecasting/metrics.py` (Day 44).

## BR-17 Supplier on-time delivery

**Formula:** on-time rate = receipts with receipt_date on or before expected_date / all receipts.

**Example:** 17 of 20 receipts on time. Rate 0.85.

**Python:** `src/analytics/suppliers.py` on_time_rate (Day 51).

## Rule changes

Any change to a threshold or formula is recorded in [DECISIONS_LOG.md](DECISIONS_LOG.md) with the reason.
