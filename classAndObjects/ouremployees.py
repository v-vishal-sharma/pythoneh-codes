#!/bin/python3

from Employees import Employees

e1 = Employees("Bob", "Sales", "Director of Sale", 120000, 10)
e2 = Employees("Linda", "Executive", "CTO", 1500000, 30)

print(e1.name)
print(e1.eligible_for_retirement())
print(e2.name)
print(e2.eligible_for_retirement())
