# Write a program that:
# Stores a list of daily expenses for a week: [45.50, 60.75, 30.25, 50.00, 70.10, 55.20, 40.00].
# Calculates and prints:
# Total weekly expenses.
# Day with the highest expense.
# Average daily expense.
# Prints a formatted summary:
# 	Total Weekly Expenses: $352.80
# Highest Expense: $70.10 on Day 5
# Average Daily Expense: $50.40



daily_expenses = [45.50, 60.75, 30.25, 50.00, 70.10, 55.20, 40.00]
total_expenses = sum(daily_expenses)


highest_expense_day = daily_expenses.index(max(daily_expenses)) + 1
average_daily_expense = total_expenses / len(daily_expenses)


print(f"Total Weekly Expenses: ${total_expenses:.2f}")
print(f"Average Daily Expense: ${average_daily_expense:.2f}")
print(f"Highest Expense: ${max(daily_expenses):.2f} on Day {highest_expense_day}")
