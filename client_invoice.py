# Q5 (Final Combined Challenge)

# This question combines almost everything you've learned about dictionaries.

# Do all of these:
# Use one loop with items().
# Print each student's name and marks.
# Calculate the total marks manually.
# Count how many students passed (marks >= 40).
# Count how many students failed (marks < 40).
# Count how many students scored 90 or above.
# Calculate the average after the loop.
# Print:
# Total marks:
# Average marks:
# Passed students:
# Failed students:
# Students with 90+:
# Rules
# ✅ Use one loop only.
# ✅ Use items().
# ✅ Do not use sum().
# ✅ Do not use extra loops.

# This is the kind of question that mixes almost every dictionary concept you've learned so far. If you solve this comfortably, the dictionary basics will be in very good shape.
students = {
    "Asha": 85,
    "Rahul": 38,
    "Pratyush": 91,
    "Riya": 76,
    "Aman": 95
}

total_marks = 0
passed = 0
failed = 0
count90 = 0

for name, marks in students.items():
    print(name, ":", marks)

    total_marks += marks

    # Pass or Fail
    if marks >= 40:
        passed += 1
        print("Passed Student:", name, ":", marks)
    else:
        failed += 1
        print("Failed Student:", name, ":", marks)

    # Independent condition
    if marks >= 90:
        count90 += 1
        print("Student with 90+:", name, ":", marks)

avg = total_marks / len(students)

print("\nTotal marks:", total_marks)
print("Average marks:", avg)
print("Passed students:", passed)
print("Failed students:", failed)
print("Students with 90+:", count90)