# **Objective:** Count occurrences of each category (string, integer) in a list.

# - **Instructions:**
#   - Initialize an empty dictionary `counts`.
#   - Loop through each element:
#     - If it's a string, check if 'str' is a key; increment its count.
#     - If it's an integer, check if 'int' is a key; increment its count.
#     - Else, do nothing (for other types).
#   - Print the counts.

list = ["apple", 2 , "banana", 4 , "cherry" , 6, 8, "kiwi", "orange", 10, 12]

counts = {'str': 0, 'int': 0}
for item in list:
    if isinstance(item, str):
        counts['str'] += 1
    elif isinstance(item, int):
        counts['int'] += 1
print("Counts:", counts)