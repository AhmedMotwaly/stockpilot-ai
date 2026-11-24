# Day 2, 24 Nov 2026: Inventory terms and first Python function

Started on the evening of 23 Nov 2026, finished on 24 Nov 2026. All numbers are simulated.

## 1. Learning objectives
- Define SKU, on hand, on order, reserved, available, inventory position, lead time and service level.
- Read Python variables, types (int, float), conditions (if/elif/else) and for loops.
- Use `stock_status` to return OK, REORDER or STOCKOUT and check it with 6 test cases.

## 2. Previous knowledge required
- Day 1: PowerShell, the virtual environment (`.venv`), Git basics.

## 3. Supply chain explanation (45 min)
- Business problem: a shelf can look full while the stock is already promised to customers,
  and a shelf can look empty while a truck is already on its way.
- Key terms:
  - **SKU**: one sellable item in one variant (for example, olive oil 1 L).
  - **On hand**: units physically in stock, according to the system.
  - **Reserved**: units promised to customer orders but not yet shipped.
  - **On order**: units ordered from the supplier but not yet received.
  - **Available** = on hand − reserved. What you can sell right now.
  - **Inventory position** = on hand + on order − reserved. What you will have once open orders arrive.
  - **Lead time**: days from placing an order to receiving it.
  - **Service level**: how often you can meet demand from stock.
- Reorder decisions use the **inventory position**, not on hand. This avoids ordering again
  when stock is already on its way.
- From the exercises (Ahmad's examples):
  - Reserved can be higher than on hand because of (1) layaway or customer orders reserved
    against future stock, (2) inventory record inaccuracy (physical stock higher than the system
    shows), or (3) stale reservations that were never released after shipping. A negative
    "available" is a **data-quality signal**, not a real stock status. Day 20 (DEL-07) will check for it.
  - On Monday morning, look at the STOCKOUT lines first. But **sales during a stockout understate
    real demand** (censored demand, or lost sales). Before lowering a reorder point, check: (1) is
    the 0 real (count it), (2) why did it run out, (3) use sales from days when stock was available.

## 4. Technical explanation (75 min)
- Variable: a name that stores a value (`on_hand = 40`).
- Types: `int` is a whole number, `float` is a number with a decimal point. A float times an int gives a float (4.50 × 12 = 54.0).
- `=` stores a value. `==` compares two values.
- Conditions: `if / elif / else`. Python checks the rules in order and stops at the first true one.
- Loops: `for x in a_list:` runs the indented lines once for each item.
- **Positional arguments**: values are matched to the `def` line by position.
  `stock_status(200, 50, 0, 100)` means on_hand=200, reserved=50, on_order=0, reorder_point=100.
- **Keyword arguments**: `stock_status(on_hand=200, reserved=50, on_order=0, reorder_point=100)`.
  These are safer, because nobody has to guess which number is which.
- `help(stock_status)` in the Python shell shows the `def` line and the description.

### The four reading patterns
| Pattern | Looks like | Warehouse meaning |
|---|---|---|
| Store | `on_hand = 40` | Write a number on the count sheet |
| Decide | `if ... elif ... else` | "If the shelf is empty, do X, otherwise do Y" |
| Repeat | `for count in shelf_counts:` | "Do this for every line on the list" |
| Running total | `total = 0`, then `total = total + count` | Add up a column, starting from zero |

Reading method for any script: (1) What goes in? (2) Which patterns are used? (3) What comes out?
Read the `print` line first.

## 5. Practical demonstration
- `scripts/practice/day02_conditions.py`: accept, partially accept or reject a customer request.
- `scripts/practice/day02_loops.py`: three customers in a row. Available stock goes down after each sale.

## 6. Step-by-step implementation (90 min)
1. Folder: `C:\Users\vanta\StockPilot-AI`
2. Terminal: PowerShell in VS Code
3. File: `src/utils/stock_status.py`

## 7. Complete code
`src/utils/stock_status.py`, rules checked in this order:
1. STOCKOUT if available <= 0
2. REORDER if inventory position <= reorder point ("at" counts)
3. OK otherwise

See the file for the full code and its 6 test cases.

## 8. PowerShell commands
| Command | What it does |
|---|---|
| `.\.venv\Scripts\python.exe src\utils\stock_status.py` | Runs the 6 test cases |
| `.\.venv\Scripts\python.exe scripts\practice\day02_reading.py` | Runs problems 8 to 10 |
| `.\.venv\Scripts\python.exe` | Opens the Python shell (`exit()` to leave) |

## 9. Expected output
```
PASS: OK
PASS: REORDER
PASS: STOCKOUT
PASS: STOCKOUT
PASS: REORDER
PASS: OK
```

## 10. Common errors and solutions
| Error message | Cause | Fix |
|---|---|---|
| `IndentationError: unexpected indent` | Spaces before a line at the `>>>` prompt | Start the line at the left edge |
| `IndentationError: expected an indented block` | No spaces inside a loop or if | Put 4 spaces before lines inside the block |
| `SyntaxError` in a practice file | Lesson text pasted into the .py file | Keep only code and `#` comments in .py files |
| Loop result is the starting value (for example `0`) | The loop never ran (typing problem in the shell) | Put multi-line code in a file and run the file |

## 11. Practical exercise (30 min): ten problems
| # | Topic | Result |
|---|---|---|
| 1 | Available = 48 − 12 | Correct (36) |
| 2 | Stock value and types | Correct (54.0; float, int, float) |
| 3 | Import and call stock_status | Ran it: OK, REORDER. Gap: positional arguments (now explained) |
| 4 | Reserved > on hand | Ran it: STOCKOUT. Strong business answer (three causes) |
| 5 | Running total of shelves | 49 (the first try showed 0 because the loop did not run in the shell) |
| 6 | Count empty shelves | Correct (2 of 5) |
| 7 | stock_status in a loop | Ran it: OK, REORDER, STOCKOUT |
| 8 | Receipts over three days | Correct (45), with a correct value trace |
| 9 | Count SKUs needing an order | Missed the boundary: 40 <= 40 counts. Answer: 2 of 4 |
| 10 | Status per shelf | Correct (OK, STOCKOUT, LOW) |

## 12. Knowledge check
- Why does the reorder decision use inventory position instead of on hand? (To avoid ordering again when stock is on its way.)
- Why does STOCKOUT come before REORDER? (The function stops at the first true rule, and a stockout is the more urgent case.)
- What does `0` mean in `stock_status(200, 50, 0, 100)`? (on_order)
- Is position 40 with reorder point 40 a reorder? (Yes. "At" counts.)

## 13. Git commit instructions
```powershell
git status
git add src/utils/stock_status.py scripts/practice docs/lessons/day-02.md PROGRESS_TRACKER.md
git commit -m "feat: add day 2 stock_status function and practice scripts"
git push
```

## 14. Completion checklist
- [x] Code runs
- [x] Tests pass (6 of 6)
- [x] Exercise done (10 problems)
- [x] Commit pushed
- [x] PROGRESS_TRACKER.md updated

## 15. Next lesson preview
Day 3: inventory KPIs (turnover, days of inventory, availability, accuracy). Python functions, lists,
dictionaries and the csv module. Build: read a 20-row CSV and compute stock value and days of cover,
then compare the result with a hand calculation.
