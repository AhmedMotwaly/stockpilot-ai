# Day 2 practice: conditions
# A new customer wants to buy some bottles. Can we sell them?
# Simulated example numbers.

on_hand = 40
reserved = 10
customer_wants = 25

available = on_hand - reserved

if customer_wants <= available:
    decision = "ACCEPT"
elif available > 0:
    decision = "PARTIAL"
else:
    decision = "REJECT"

print("Available:", available)
print("Customer wants:", customer_wants)
print("Decision:", decision)