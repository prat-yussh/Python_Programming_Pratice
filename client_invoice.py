# Dictionary Q2 (Combined)

# Do all of these:

# Print all keys.
# Print all values.
# Print all key-value pairs.
# Check whether the key "email" exists.
# If it exists, print "Email available".
# Otherwise, print "Email not available".
# Add:
# "email": "asha@company.com"
# Print the updated dictionary.
# New methods you'll practice
# employee.keys()
# employee.values()
# employee.items()

employee = {
    "id": "EMP101",
    "name": "Asha",
    "department": "IT",
    "salary": 45000
}

print(employee.keys())
print(employee.values())
print(employee.items())

if "email" in employee.keys():
    print("Email available")
else:
    print("Email not available")

employee["email"] = "asha@company.com"
print(employee)