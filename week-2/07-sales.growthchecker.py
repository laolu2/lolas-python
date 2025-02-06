# Write a program that:
# Stores two lists representing sales for two years:
# python
# Copy code
# year_1_sales = [4000, 4500, 4700, 5000, 5200, 4800]
# year_2_sales = [4200, 4600, 4800, 5100, 5300, 4900]


# Uses a loop and conditions to identify months with sales growth greater than 5%.
# Prints the month and percentage growth for those months:
# sql
# Copy code
# Month 2: Growth = 6.67%


year_1_sales = [4000, 4500, 4700, 5000, 5200, 4800]
year_2_sales = [4200, 4600, 4800, 5100, 5300, 4900]

for month, (year_1_sales, year_2_sales) in enumerate(zip(year_1_sales, year_2_sales), start=1):
         growth_percentage = ((year_2_sales - year_1_sales) / year_1_sales) * 100
print(f"Month {month}: Growth = {growth_percentage:.2f}%")


