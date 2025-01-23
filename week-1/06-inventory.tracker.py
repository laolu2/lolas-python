# Inventory Tracker
# Write a program that:
# Creates a list of items in stock, e.g., ["apples", "bananas", "oranges", "grapes"].
# Asks the user to enter an item they want to check.
# Checks if the item is in the stock list:
# If yes, prints: "Yes, we have [item] in stock."
# If no, prints: "Sorry, we don't have [item]."
# Asks the user how many of the item they want to buy and calculates the total cost based on a random price (e.g., 2.5 per item).
# Prints the receipt like:
# 	You bought 3 bananas for 7.50. Thank you for shopping!




# List of items in stock
stock = ["apples", "bananas", "oranges", "grapes"]
item = input("Enter the item you want to check: ")


if item in stock:
    print(f"Yes, we have {item} in stock.")
    quantity = int(input(f"How many {item} do you want to buy? "))
    price_per_item = 4.5
    total_cost = quantity * price_per_item
    print(f"You bought {quantity} {item} for {total_cost:.2f}. Thank you for shopping!")
else:
    print(f"Sorry, we don't have {item}.")