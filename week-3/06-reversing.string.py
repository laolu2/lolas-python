# *Objective:** Reverse a string using loops.

# - **Instructions:**
#   - Initialize an empty list `reversed_chars`.
#   - Loop from the end of the string to the beginning.
#     - For each index, append the character to `reversed_chars`.
#   - Join and print the reversed characters.


input_string = 'Hello, world!'

reversed_chars = []
for i in range ((len(input_string) -1), -1, -1):
    reversed_chars.append(input_string[i])
    
    reversed_string = '' .join(reversed_chars)
print(reversed_string)