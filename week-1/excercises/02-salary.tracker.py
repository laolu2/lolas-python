employees = ["Alice", "Bob", "Charlie", "Diana"]
salaries = [55000, 48000, 62000, 47000]
new_salaries = [salary * 1.10 for salary in salaries]

for i in range(len(employees)):
    old_salary = salaries[i]
    new_salary = new_salaries[i]
    print(f"{employees[i]}: Old Salary = ${old_salary:,}, New Salary = ${new_salary:,.0f}")