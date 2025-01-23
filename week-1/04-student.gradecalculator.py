# List of students
students = ["Alice", "Bob", "Charlie"]
scores = {}


for student in students:
    scores[student] = {}
    scores[student]["Math"] = int(input(f"Enter {student}'s Math score: "))
    scores[student]["Science"] = int(input(f"Enter {student}'s Science score: "))
    scores[student]["English"] = int(input(f"Enter {student}'s English score: "))


for student in students:
    total_score = sum(scores[student].values())
    average_score = total_score / 3
    print(f"{student}'s total score is {total_score}, and their average score is {average_score:.2f}.")