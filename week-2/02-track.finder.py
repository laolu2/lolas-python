# Write a program that:
# Stores a list of sales numbers: [4500, 5600, 6100, 4700, 4900, 5200].
# Uses a loop and a condition to find the sales numbers greater than 5000.
# Prints each qualifying sales number and its month (assume Month 1 corresponds to the first number).
# yaml
# Copy code
# Month 2: Sales = 5600
# Month 3: Sales = 6100



sales = [4500, 5600, 6100, 4700, 4900, 5200]

for month, sale in enumerate(sales, start=1):
    if sale > 5000:
        print(f"Month {month}: Sales = {sale}")


