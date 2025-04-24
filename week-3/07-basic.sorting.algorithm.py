# **Objective:** Sort a list using the bubble sort algorithm with loops.

# - **Instructions:**
#   - Loop through the list multiple times until no swaps are needed.
#     - For each element, compare it with the next one.
#     - If in wrong order, swap them and set a flag to indicate a change.
#   - Continue until a pass with no changes occurs.


list = [10, 20, 30, 10, 82, 40, 45, 50, 55, 30, 22, 35]

# buuble sort algorithm
for i in range((len(list) -1), 0, -1):
    for i in range (0, i):
        if list[i] > list[i + 1]:
            #  swap
            temp = list[i]
            list[i] = list [i + 1]
            list[i + 1] = temp
print(list)
