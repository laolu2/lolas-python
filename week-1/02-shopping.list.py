# Asks the user for their budget (a float) and saves it in a variable.
# Asks the user to input a comma-separated list of items they want to buy (e.g., apple, banana, orange) and saves it as a list.
# Prints the total number of items in the list using string formatting.
# Calculates how much each item would cost if the budget is divided evenly among the items.
# Prints a statement like:
# 	With a budget of 100.0, each item will cost 33.33.


# Ask user for budget
budget = float(input("Enter a budget: "))

# Ask user for items they want to buy
items_to_buy = input("Enter comma-seperated list of items to buy: ")

items = items_to_buy.split(",")

print("Total number of items: %d" % len(items) )

item_cost = budget / len(items)

print("With a budget of %.2f, each item will cost %.2f" % (budget, item_cost))