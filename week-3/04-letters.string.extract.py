# **Objective:** Extract only alphabetic characters from a string.

# - **Instructions:**
#   - Initialize an empty list `letters`.
#   - Loop through each character in the string.
#   - For each char, check if it's alpha:
#     - If yes, add to `letters` list.
#     - Else, skip.
#   - Print the resulting list.



letters = []

input_string = "Hello, World! 123"
for char in input_string:
    if char.isalpha():
     letters.append(char)

print(letters)

