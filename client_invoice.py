# Q5 is complete. ✅

# PDF 4.1 — Q6: Student Result Processor

# A school stores marks for three students:

student_names = ["Asha", "Rahul", "Pratyush"]

student_marks = [
    [78, 65, 81],
    [55, 32, 62],
    [90, 88, 92]
]

# Each inner list contains marks for three subjects.

# Build a program that does exactly this

# For each student:
for i in range(len(student_names)):
    student = student_names[i]
    marks = student_marks[i]

    total = 0
    status = "Pass"

    for mark in marks:
        total = total + mark
        if mark < 40:
            status = "Fail"
    
    avg = total/len(marks)
        
    print("Student:",student)
    print("Total:",total)
    print("Average:{:.2f}".format(avg))
    print("Status:",status)
# Calculate the total marks manually.
# Calculate the average marks.
# Check all three subjects:
# if any subject mark is below 40, status is "Fail";
# otherwise, status is "Pass".
# Print:
# Student: Asha
# Total: 224
# Average: 74.67
# Status: Pass
# After processing all students, print:
# Passed students:
# Failed students:
# Rules
# Use one loop for students.
# Use another loop inside it for that student’s marks.
# Do not use sum(), min(), or max().
# Show the average with two decimal places.