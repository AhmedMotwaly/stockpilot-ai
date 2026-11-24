"""Day 2 practice: stock status for one SKU in one location.

Simulated data only.
"""


def stock_status(on_hand, reserved, on_order, reorder_point):
    """Return "STOCKOUT", "REORDER" or "OK" for one SKU.

    Rules, checked in this order:
    1. STOCKOUT: available (on_hand - reserved) is 0 or less.
    2. REORDER: inventory position (on_hand + on_order - reserved)
       is at or below reorder_point.
    3. OK: anything else.
    """
    # ---- YOUR CODE STARTS HERE ----
    # Calculate available stock
    available = on_hand - reserved
    # Calculate inventory position
    inventory_position = on_hand + on_order - reserved

    if available <= 0:
        return "STOCKOUT"
    elif inventory_position <= reorder_point:
        return "REORDER"
    else:
        return "OK"
    # ---- YOUR CODE ENDS HERE ----


def check(on_hand, reserved, on_order, reorder_point, expected):
    """Run stock_status once and print PASS or FAIL."""
    result = stock_status(on_hand, reserved, on_order, reorder_point)
    if result == expected:
        print("PASS:", result)
    else:
        print("FAIL: got", result, "but expected", expected)


if __name__ == "__main__":
    # check(on_hand, reserved, on_order, reorder_point, expected)
    check(120, 30, 200, 150, "OK")         # 1. plenty of stock
    check(60, 20, 0, 100, "REORDER")       # 2. position 40, below 100
    check(10, 10, 300, 100, "STOCKOUT")    # 3. empty shelf, truck coming
    check(15, 15, 0, 60, "STOCKOUT")       # 4. both rules true: stockout wins
    check(70, 10, 0, 60, "REORDER")        # 5. position exactly 60: "at" counts
    check(71, 10, 0, 60, "OK")             # 6. position 61: just above