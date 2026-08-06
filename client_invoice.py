# Q4 (Combined + Loop)

# Now let's combine dictionaries with loops.


# Do all of these:

# Create:
# Use one loop with items() to:
# Print each subject and its marks like:
# Math : 85
# Science : 92
# Calculate the total marks manually.
# Calculate the average after the loop.
# Find how many subjects have marks 90 or above.
# Print:
# Total:
# Average:
# Subjects with 90+:
# Rules
# Use one loop only.
# Use items().
# Do not use sum().

# This question combines:

# Dictionaries
# Loops
# Manual calculations
# Conditions

# This is the type of question you'll often see in interviews and coding tests.

marks = {
    "Math": 85,
    "Science": 92,
    "English": 78,
    "Computer": 95
}

total = 0
count_90 = 0

for subject,value in marks.items():
    print(subject,":",value)
    total = total + value

    if value > 90:
        count_90 += 1  

avg = total / len(marks)
print(total)
print(avg)
print("Subjects with 90+:", count_90)
