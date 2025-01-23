# #Write a program that:
# #Prints a welcome message for the quiz, like:
# 	Welcome to the Python Basics Quiz!
# #Asks the user three multiple-choice questions:
#  Q1: What is the output of print("Hello, World!")?
# Q2: What data type is used to store a list of items?
# Q3: What operator is used to raise a number to a power?
# Stores the user's answers in a list.
# Compares the answers with the correct answers (["Hello, World!", "list", "**"]).
# Calculates and formats the user's score as a percentage, printing:
# 	You got 2 out of 3 questions correct. That's 66.67%!


print('Welcome to the Python Basics Quiz')

Q1 = input('Q1: What is the output of print("Hello, World!")? ')
Q2 = input('Q2: What data type is used to store a list of items? ')
Q3 = input('Q3: What operator is used to raise a number to a power? ')

my_list = [Q1, Q2, Q3]

correct_answers = ["Hello, World!", "list", "**"]
number_of_correct_answers = 0

for i in range(3):
    if my_list[i] == correct_answers[i]:
        number_of_correct_answers += 1

score = (number_of_correct_answers / 3) * 100
print(f"You got {number_of_correct_answers} out of 3 questions correct. That's {score:.2f}%!")