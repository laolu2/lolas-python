# 1. Sales Data Insights
# Write a program that:
# Creates a list of monthly sales numbers: [4500, 5600, 6100, 4700, 4900, 5200].
# Calculates and prints:
# Total sales for the 6 months.
# Average monthly sales.
# The month with the highest sales.
#Formats and prints the results like:
# Total Sales: $31,000
# Average Monthly Sales: $5,166.67
# Highest Sales: $6,100 (Month 3)


sales =  [4500, 5600, 6100, 4700, 4900, 5200]

total_sales = sum(sales)
average_sales = total_sales / len(sales)

# Find the month with the highest sales
highest_sales = max(sales)
highest_month = sales.index(highest_sales) + 1

print(f"Total Sales: ${total_sales:}")
print(f"Average Monthly Sales: ${average_sales:.2f}")
print(f"Highest Sales: ${highest_sales} (Month {highest_month})")







