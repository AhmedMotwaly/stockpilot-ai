# Day 2 practice: reading code (problems 8 to 10)
# Read each problem, write your prediction, then run this file.
# Simulated example numbers.

# ---- Problem 8: goods received over three days ----
receipts = [20, 0, 15]
on_hand = 10
for received in receipts:
    on_hand = on_hand + received
print("Problem 8:", on_hand)


# ---- Problem 9: how many SKUs need an order? ----
positions = [90, 40, 15, 60]
reorder_point = 40
need_order = 0
for position in positions:
    if position <= reorder_point:
        need_order = need_order + 1
print("Problem 9:", need_order, "of", len(positions), "SKUs need an order")


# ---- Problem 10: a status for each shelf ----
for available in [25, 0, 8]:
    if available <= 0:
        status = "STOCKOUT"
    elif available <= 10:
        status = "LOW"
    else:
        status = "OK"
    print("Problem 10:", available, status)
