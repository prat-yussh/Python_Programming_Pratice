# Q3: Weekly Expense Analyzer

# The user enters five daily expenses in one line:

# Enter 5 expenses: 500 1200 300 2500 700
# Exact requirements

expenses = [int(value) for value in input("Enter 5 expenses: ").split()]

# Using a for loop:

# Calculate the total expense.
# Count how many expenses are greater than 1000.
# Print each expense greater than 1000 with this message:
# High expense: 1200
# After the loop, print:
# Total expense:
# Number of high expenses:

total_expenses = 0
total_expenses_count = 0

for expense in expenses:
    total_expenses = total_expenses + expense

    if expense > 1000:
        total_expenses_count = total_expenses_count + 1
        print("High expense:",expense)

print("Total expenses:",total_expenses)
# Do not use sum() or count(). Calculate both values manually inside the loop.