# **Objective:** Count occurrences of each value in a list.

# - **Instructions:**
#   - Initialize an empty dictionary `counts`.
#   - Loop through each number in the dataset.
#     - Check if it's already a key; increment its count.
#     - Else, add it with a count of 1.
#   - Print the counts.

numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3]

counts = {}

for number in numbers:
    if number in counts:
        counts[number] += 1
    else:
        counts[number] = 1
print("counts:", counts)


