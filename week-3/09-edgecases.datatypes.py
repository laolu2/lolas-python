# **Objective:** Identify and print non-numeric values in a list.

# - **Instructions:**
#   - Loop through each element.
#     - Check if the element is of type `int` or `float`.
#       - If yes, continue to next iteration.
#       - Else, print it as a non-numeric value.


list = [10, 20, 30, 40, "a", 50, None, 60, "b", 70, 80, 90, 100]

for element in list:
    if not isinstance(element, (int, float)):
        print(element, "is a non-numeric value")
