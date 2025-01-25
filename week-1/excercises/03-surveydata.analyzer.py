#  Survey Data Analyzer
# Write a program that:
# Asks the user to input survey responses as a comma-separated list (e.g., "Yes, No, Yes, Yes, No, Maybe").
# Splits the string into a list.
# Calculates the count of each response (Yes, No, Maybe).
# Prints a summary:
# Survey Summary:
# Yes: 3
# No: 2
# Maybe: 1



survey_responses = input("Enter survey responses as a comma-separated list: ")
comma_separated_list = survey_responses.split(", ")

count_yes = comma_separated_list.count("Yes")
count_no = comma_separated_list.count("No")
count_maybe = comma_separated_list.count("Maybe")


print("Survey Summary:")
print(f"Yes: {count_yes}")
print(f"No: {count_no}")
print(f"Maybe: {count_maybe}")