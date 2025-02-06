# Write a program that:
# Stores daily temperatures for a week in Fahrenheit: [72, 75, 78, 74, 71, 69, 73].
# Uses a loop and conditions to:
# Count how many days were above 75°F.
# Convert all temperatures to Celsius and print them.
# Prints the number of hot days and the Celsius temperatures:
# yaml
# Copy code
# Hot Days: 2


temperatures_fahrenheit = [72, 75, 78, 74, 71, 69, 73]
hot_days = 0

for index, temp_f in enumerate(temperatures_fahrenheit, start=1):
    if temp_f > 75:
        hot_days += 1
    temp_c = (temp_f - 32) * 5/9
    temperatures_fahrenheit[index-1] = temp_c
print(f"Hot Days: {hot_days}\n{[f'{temp:.2f}' for temp in temperatures_fahrenheit]}")