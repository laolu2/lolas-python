students = ["Alice", "Bob", "Charlie", "Diana"]
grades = [85, 92, 78, 90]

for student, grade in zip(students, grades):
    if grade >= 90:
        category = "Excellent"
    elif grade >= 80:
        category = "Good"
    else:
        category = "Needs Improvement"
    print(f"{student}: Grade = {grade}, Category = {category}")