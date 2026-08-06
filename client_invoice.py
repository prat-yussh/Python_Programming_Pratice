# Dictionary Q1 (Combined)

# Do all of these:

# Print the student's name.
# Print the student's CGPA.
# Change the CGPA to 8.4.
# Add a new key:
# "college": "Centurion University"
# Print the complete dictionary.
# Print the total number of key-value pairs using len().

# This single question covers:

# Accessing values
# Updating values
# Adding new keys
# Printing the dictionary
# Using len()

student = {
    "name": "Pratyush",
    "branch": "CSE",
    "semester": 7,
    "cgpa": 8.1
}

print("Students name:",student["name"])
print("Students CGPA:",student["cgpa"])

student["cgpa"] = 8.4
student["college"] = "Centurion University"

print(student)
print(len(student))