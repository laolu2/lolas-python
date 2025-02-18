# Write a program that:
# Asks the user to enter daily sales numbers (one at a time).
# Uses a loop to calculate a running total of sales. The loop should stop when the user enters a negative number.
# Prints the total sales:
# bash
# Copy code
# Total Sales: $15,000


total_sales = 0.0

while True:
    sales = float(input("Enter daily sales number (enter a negative number to stop): "))
    if sales < 0.0:
        break
    total_sales += sales

print(f"Total Sales: ${total_sales}")