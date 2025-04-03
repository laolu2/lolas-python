# **Objective:** Identify unique elements in a list.

# - **Instructions:**
#   - Initialize an empty list `seen`.
#   - Loop through each element in the dataset.
#     - If the element is not in `seen`, add it to both `seen` and `unique`.
#     - Else, skip adding to `unique`.
#   - Print the unique elements.

seen = []
unique = []
list = [10, 20, 10, 40, 30, 20, 50, 60, 70, 80, 90, 100, 10, "a", "b", "a"]

for element in list:
    if element not in seen:
        seen.append(element)
        unique.append(element)
    else:
        print("skipping", element)
        continue
    print("adding", element, " to", seen)
    print("adding", element, "to", unique)

print(unique)

