# Write a program that:

# Stores a list of product descriptions:
# 	descriptions = [
# "Red Apple - Fresh and Sweet",
# "Yellow Banana - Rich in Potassium",
# "Green Grapes - Seedless and Juicy"
# ]
# Asks the user to input a keyword (e.g., "Red" or "Sweet").
# Searches the descriptions for the keyword and prints any matches, formatted like:
# 	Found Matches:
# - Red Apple - Fresh and Sweet


product_descriptions = [
"Red Apple - Fresh and Sweet",
"Yellow Banana - Rich in Potassium",
"Green Grapes - Seedless and Juicy"]

keyword = input("Enter a keyword to search in product descriptions: ")
found_matches = [description for description in product_descriptions  if keyword.lower() in description.lower()]

print("Found Matches:")
for match in found_matches:
    print("-", match)
