# Write a program that:
# Creates a list of student names and their test scores:
# 	students = ["Alex", "Brian", "Chloe", "Diana"]
# scores = [88, 92, 79, 95]
# Finds and prints the names of students who scored above 90.
# Calculates and prints the average score.



students = ["Alex", "Brian", "Chloe", "Diana"]
scores = [88, 92, 79, 95]


high_scorers = [student for student, score in zip(students, scores) if score > 90]
average_score = sum(scores) / len(scores)


print("Students who scored above 90:", high_scorers)
print("\nAverage Score:", average_score)