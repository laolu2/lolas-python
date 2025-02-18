# Write a program that:
# Stores a list of expenses and their categories:
# python
# Copy code
# expenses = [("Rent", 1200), ("Groceries", 300), ("Utilities", 150), ("Dining", 100), ("Travel", 400)]


# Uses a loop to:
# Calculate the total spent on each category.
# Identify categories where the spending is above $300.
# Prints a summary:
# bash
# Copy code
# Rent: $1200 (Above Threshold)
# Groceries: $300


expenses = [("Rent", 1200), ("Groceries", 300), ("Utilities", 150), ("Dining", 100), ("Travel", 400)]

for category, amount in expenses:
    if amount > 300:
        print(f"{category}: ${amount} (Above Threshold)")
    else:
        print(f"{category}: ${amount}")
