# Q14: Combine and Repeat Task Lists

# Do exactly this:

# Combine morning_tasks and evening_tasks using +.
# Store the result in daily_tasks.
# Print daily_tasks.
# Compare daily_tasks with expected_tasks using ==.
# Print:
# Task order correct

# or:

# Task order incorrect
# Create two_day_tasks by repeating daily_tasks two times using *.
# Print two_day_tasks.

# Do not use a loop or list methods.

# Lists support + for concatenation and * for repetition. List equality checks the values and their order.

morning_tasks = ["Email", "Meeting"]
evening_tasks = ["Report", "Backup"]
expected_tasks = ["Email", "Meeting", "Report", "Backup"]

daily_tasks = morning_tasks + evening_tasks
print(daily_tasks)
if daily_tasks == expected_tasks:
    print("TAsk order correct")
else:
    print("TAsk order incorrect")


two_day_task = daily_tasks * 2
print(two_day_task)