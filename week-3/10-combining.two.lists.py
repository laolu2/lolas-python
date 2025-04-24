# **Objective:** Create pairs from two lists of equal length.

# - **Instructions:**
#   - Loop through the indices.
#     - For each index, pair elements from both lists into tuples.
#   - Collect these tuples in a new list and print them.

list1 = [1, 2, 3]
list2 = ["a", "b", "c"]

pairs = []
for i in range(len(list1)):
    pairs.append((list1[i], list2[i]))

print(pairs)
