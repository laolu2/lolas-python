# Write a program that:
# Stores weekly temperature readings in a list: [72, 75, 78, 74, 71, 69, 73].
# Converts the temperatures to Celsius (use the formula (F - 32) * 5/9) and stores them in a new list.
# Calculates and prints:
# Average weekly temperature in Fahrenheit and Celsius.
# Day(s) with the highest temperature.




weekly_temperatures_fahrenheit = [72, 75, 78, 74, 71, 69, 73]
weekly_temperatures_celsius = [(temp - 32) * 5/9 for temp in weekly_temperatures_fahrenheit]

average_temp_fahrenheit = sum(weekly_temperatures_fahrenheit) / len(weekly_temperatures_fahrenheit)
average_temp_celsius = sum(weekly_temperatures_celsius) / len(weekly_temperatures_celsius)


print(f"Average weekly temperature: {average_temp_fahrenheit}°F ({average_temp_celsius:.2f}°C)")
