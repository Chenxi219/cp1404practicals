"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
"""
get sales
while sales >= 0
    if sales < 1000
       bonus = sales * 10%
    else
       bonus = sales * 15%
display bonus
"""
LOW_LEVEL = 0.1
HIGH_LEVEL = 0.15
MINIMUM_SALES = 0
MAXIMUM_SALES = 1000

sales = float(input("Enter sales: $"))
while sales < MINIMUM_SALES:
    print("Invalid input")
    sales = float(input("Enter sales: $"))
if sales < MAXIMUM_SALES:
    bonus = sales * LOW_LEVEL
else:
    bonus = sales * HIGH_LEVEL
print(f"Bonus is {bonus}")