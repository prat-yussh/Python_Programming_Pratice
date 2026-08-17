# Dictionary Q7 — Nested Dictionary + Loop

# Now let's do one important nested-dictionary question and then move toward finishing dictionaries.

# Do all of these:

# Print Riya's salary.
# Loop through the outer dictionary using items().

# For each employee, print:

# EMP101 : Asha : 45000
# Count how many employees are in the "IT" department.
# Find the highest salary manually.

# Print:

# IT employees:
# Highest salary:
# Rules
# Use one loop.
# Use items().
# Do not use max().
# Don't create another loop.

employees = {
    "EMP101": {
        "name": "Asha",
        "department": "IT",
        "salary": 45000
    },
    "EMP102": {
        "name": "Rahul",
        "department": "HR",
        "salary": 38000
    },
    "EMP103": {
        "name": "Riya",
        "department": "IT",
        "salary": 52000
    }
}

it_dept=0
highest_salary = 0
highest_salary_emp_id = 0


# print(employees)
for employe_id,details in employees.items():
    print(employe_id,details["name"],details["salary"],sep=" : ")
    if details["department"] == "IT":
        it_dept += 1
        print("IT employees:",details["name"])
    if details["salary"] > highest_salary:
        highest_salary_emp_id = employe_id
        highest_salary = details["salary"]
        
print("Highest salary:",highest_salary)
    