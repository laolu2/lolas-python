# Write a program that:
# Stores votes for candidates in a list:
# python
# Copy code
# votes = ["Alice", "Bob", "Alice", "Charlie", "Alice", "Bob", "Charlie", "Charlie"]


# Uses a loop and conditions to count votes for each candidate.
# Prints the results:
# makefile
# Copy code
# Alice: 3 votes
# Bob: 2 votes


votes = ["Alice", "Bob", "Alice", "Charlie", "Alice", "Bob", "Charlie", "Charlie"]
vote_count = {}

for candidate in votes:
    if candidate in vote_count:
        vote_count[candidate] += 1
    else:
        vote_count[candidate] = 1

for candidate, count in vote_count.items():
    print(f"{candidate}: {count} votes")
