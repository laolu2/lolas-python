# Write a program that:
# Creates a list of product prices (some containing invalid entries): ["$25", "$30", "N/A", "$40", "error", "$50"].
# Cleans the data by:
# Removing invalid entries ("N/A" and "error").
# Converting valid prices to integers.
# Prints the cleaned list and the total sum of the prices.


product_prices = ["$25", "$30", "N/A", "$40", "error", "$50"]
cleaned_prices = [int(price.strip('$')) for price in product_prices if price[0] == '$']

# Calculate the total sum of the cleaned prices
total_sum = sum(cleaned_prices)

print("Cleaned List of Product Prices:" , cleaned_prices)
print(f"\nTotal Sum of Prices: ${total_sum}")