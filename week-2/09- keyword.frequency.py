# Write a program that:
# Stores a list of sentences:
# python
# Copy code
# sentences = [
#     "Python is great for data analysis.",
#     "Data analysts use Python and SQL.",
#     "Data visualization is key in analysis.",
#     "Learn Python for data analysis."
# ]


# Uses a loop and conditions to count how many sentences contain the keyword "data".
# Prints the frequency of the keyword:
# arduino
# Copy code
# The keyword 'data' appears in 3 sentences.



sentences = [
    "Python is great for data analysis.",
    "Data analysts use Python and SQL.",
    "Data visualization is key in analysis.",
    "Learn Python for data analysis."
]

keyword = "data"
count = 0

for sentence in sentences:
    if keyword in sentence.lower():
        count += 1

print(f"The keyword '{keyword}' appears in {count} sentences.")
