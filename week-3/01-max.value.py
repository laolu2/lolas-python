# **Objective:** Find the maximum value in a list without using built-in functions.

# - **Instructions:**
#   - Initialize `max_value` with the first element.
#   - Loop through each number in the list starting from the second element.
#   - If the current number is greater than `max_value`, update `max_value`.
#   - After processing all elements, print the maximum value.


list = [10,20,30,23,82, 18,9,89, 73, 81, 10]


max_value = list[0]
print(max_value)

for x in range(1, len(list)):
    print("comparing", max_value, " and ", list[x])
    if list[x] > max_value:
        max_value = list[x]

print(max_value)