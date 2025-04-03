# **Objective:** Calculate the mean (average) of a list.

# - **Instructions:**
#   - Initialize `sum` to 0.
#   - Loop through each element in the list, adding each to `sum`.
#   - After the loop, divide `sum` by the length of the list to get the mean.
#   - Print the result.


list = [10,20,30,23,82,18,9,89, 73, 81, 10]

# SOLUTION 1
sum = 0
print(sum)

for x in range(0, len(list)):
    print("adding", list[x], " to ", sum)
    sum += list[x]

print(sum)

mean = sum / len(list)
print(mean)


# SOLUTION 2
sum = 0
print(sum)

for x in range(0, len(list)):
   sum += list[x]

print(sum)

mean = sum / len(list)
print(mean)