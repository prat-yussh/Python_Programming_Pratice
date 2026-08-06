# Q10: Remove Duplicate Course Names

# Do exactly this:

# Convert the list into a set named unique_courses.
# Print unique_courses.
# Convert the set back into a list named course_list.
# Print course_list.
# Print the total number of unique courses.

# Use only:

# set()
# list()
# len()

# Do not use a loop.

# Important

# The order of course_list may be different from the original because sets do not preserve order.

# This question teaches one of the most common real-world uses of sets: removing duplicates from a list.

courses = [
    "Python",
    "Java",
    "Python",
    "C++",
    "Java",
    "SQL"
]

unique_courses = set(courses)
print(unique_courses)
course_list = list(unique_courses)
print(course_list)
print(len(course_list))