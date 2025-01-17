
#Write a program that:
#Stores a list of students' names: ["Alice", "Bob", "Charlie"].
#Asks the user to input their scores for three subjects (Math, Science, and English).
#Calculates the total score and average for each student.
#Formats and prints the results like:
	#Alice's total score is 270, and their average score is 90.00.



    # List of students' names
from pyexpat.errors import codes


students = ["Alice", "Bob", "Charlie"]

# Ask the user to input scores for each student
for student in students:
    print(f"Enter the scores for {students}:")
    math = int(input("  Math: "))
    science = int(input("  Science: "))
    english = int(input("  English: "))
    [student] = [math, science, english]

# Calculate and display total and average scores
for student, score_list in codes.items():
    total = sum(score_list)
    average = total / len(score_list)
    print (student) total score is (total) and their average score is {average:.2f}.")

