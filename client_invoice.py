# Dictionary Q6 — get() + update() + condition

# You have:

# Do all of this:

# Use get() to retrieve "name".
# Use get() to retrieve "email" with "Not available" as the default value.

# Use update() to add:

# "email": "asha@company.com"
# "experience": 2
# Increase the salary to 50000.
# Print the final dictionary.

# No loop needed.

employee = {
    "name": "Asha",
    "department": "IT",
    "salary": 45000
}

employee.update({"email": "asha@company.com","experience": 2,"salary": 50000})
print(employee.get(["name"]))
print(employee.get("email","Not available"))
print(employee)