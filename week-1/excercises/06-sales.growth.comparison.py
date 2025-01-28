# Write a program that:
# Creates two lists representing sales for two years:
# 	year_1_sales = [4000, 4500, 4700, 5000, 5200, 4800]
# year_2_sales = [4200, 4600, 4800, 5100, 5300, 4900]
# Calculates:
# Monthly growth percentage: ((Year 2 - Year 1) / Year 1) * 100.
# Overall sales growth for the year.
# Prints a formatted report showing the monthly and total growth.


year_1_sales = [4000, 4500, 4700, 5000, 5200, 4800]
year_2_sales = [4200, 4600, 4800, 5100, 5300, 4900]

monthly_growth_percentage = [((year_2 - year_1) / year_1) * 100 for year_1, year_2 in zip(year_1_sales, year_2_sales)]
overall_sales_growth = ((sum(year_2_sales) - sum(year_1_sales)) / sum(year_1_sales)) * 100


print("Monthly Growth Percentage:")
for i, growth in enumerate(monthly_growth_percentage):
    print(f"Month {i+1}: {growth:.2f}%")

print(f"Overall Sales Growth for the year: {overall_sales_growth:.2f}%")

