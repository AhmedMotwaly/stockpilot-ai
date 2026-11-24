# Day 2 practice: loops
# Three customers arrive one after another. Check each request.
# Available stock goes down after every sale.
# Simulated example numbers.

available = 30
requests = [10, 25, 40]

for customer_wants in requests:
    if customer_wants <= available:
        decision = "ACCEPT"
        available = available - customer_wants
    elif available > 0:
        decision = "PARTIAL"
        available = 0
    else:
        decision = "REJECT"
    print("Customer wants", customer_wants, "->", decision, "| left:", available)

print("Done. Checked", len(requests), "requests.")