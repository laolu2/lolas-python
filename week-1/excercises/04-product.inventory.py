# Write a program that:
# Creates a list of products with their quantities:
# 	products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
# quantities = [15, 50, 20, 10]
# Allows the user to:
# Check the quantity of a product.
# Update the quantity after a sale.
# Prints the updated inventory list after each sale.



products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
quantities = [15, 50, 20, 10]

while True:
    print("Current Inventory:")
    for product, quantity in zip(products, quantities):
        print(f"{product}: {quantity}")

    user_input = input("Enter product to check/update quantity (or 'exit' to end): ")
    if user_input.lower() == 'exit':
        break
    elif user_input in products:
        index = products.index(user_input)
        current_quantity = quantities[index]
        print(f"The current quantity of {user_input} is: {current_quantity}")

        update_quantity = int(input("Enter the new quantity after sale: "))
        quantities[index] = update_quantity

        print("Updated Inventory:")
        for product, quantity in zip(products, quantities):
            print(f"{product}: {quantity}")
    else:
        print("Product not found. Please try again.")