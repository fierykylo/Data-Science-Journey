employees = [
    ("Aarush", "IT", 50000),
    ("Rahul", "HR", 30000),
    ("Neha", "IT", 45000),
    ("Priya", "Finance", 28000)
]

# 1. Employees in IT department
print("Employees in IT department:")
for emp in employees:
    name, dept, salary = emp
    if dept == "IT":
        print(name)


# 2. Total salary
total_salary = 0
for emp in employees:
    total_salary += emp[2]

print("\nTotal Salary:", total_salary)


# 3. Employee with lowest salary
min_emp = employees[0]

for emp in employees:
    if emp[2] < min_emp[2]:
        min_emp = emp

print("\nEmployee with lowest salary:", min_emp[0], "-", min_emp[2])