# Product Restock Alert
# Write a program that:
# Stores a list of product quantities:
# python
# Copy code
# products = ["Apples", "Bananas", "Oranges", "Grapes"]
# quantities = [5, 2, 15, 0]
# Uses a loop and conditions to identify products that need restocking (quantity less than 5).
# Prints a restock alert for those products:
# yaml
# Copy code
# Restock Alert: Bananas (2 remaining)
# Restock Alert: Grapes (0 remaining)



products = ["Apples", "Bananas", "Oranges", "Grapes"]
quantities = [5, 2, 15, 0]

for product, quantity in zip(products, quantities):
    if quantity < 5:
        print(f"Restock Alert: {product} ({quantity} remaining)")