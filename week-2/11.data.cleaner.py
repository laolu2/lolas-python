# Write a program that:
# Stores a list of mixed data entries: [100, "N/A", 200, "Error", 300, "N/A", 400].
# Uses a loop and conditions to clean the data by:
# Removing "N/A" and "Error".
# Keeping only numerical values.
# Prints the cleaned data and the sum of valid entries:
# yaml
# Copy code
# Cleaned Data: [100, 200, 300, 400]
# Total: 1000


data_entries = [100, "N/A", 200, "Error", 300, "N/A", 400]
cleaned_data = []
total = 0

for entry in data_entries:
    if isinstance(entry, int):
        cleaned_data.append(entry)
        total += entry

print(f"Cleaned Data: {cleaned_data}")
print(f"Total: {total}")
