# Daily Expense Tracker
# Write a program that:
# Stores a list of daily expenses for a week: [45.50, 60.75, 30.25, 50.00, 70.10, 55.20, 40.00].
# Uses a loop to:
# Identify which days had expenses above the average.
# Print the expense and the day for each above-average expense:
# bash
# Copy code
# Day 2: $60.75 (Above Average)
# Day 5: $70.10 (Above Average)



expenses = [45.50, 60.75, 30.25, 50.00, 70.10, 55.20, 40.00]
average_expense = sum(expenses) / len(expenses)

for day, expense in enumerate(expenses, start=1):
    if expense > average_expense:
        print(f"Day {day}: ${expense:.2f} (Above Average)")





