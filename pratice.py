# Q3: Sales Report Generator

# A shop employee records sales for three days.

# Input

# Ask the user to enter:

# Employee name
# Sales for Day 1, Day 2, and Day 3 in one line separated by spaces
# Weekly sales target

# Example:

# Employee name: Pratyush
employee_name = input("Employee name:")
# Enter 3 sales amounts: 2500 3200 2800
day1,day2,day3 = [float(value) for value in input("Enter 3 sales amounts:").split(',')]
# Enter target: 8000
# Program requirements
# Store the employee name as a string.
# Separate the three sales values from the single input.
# Convert each sales value to float.
# Convert the target to float.
target = float(input("Traget:"))
# Calculate:
# Total sales = Day 1 + Day 2 + Day 3
total_sales = day1+day2+day3
# Average sales = Total sales ÷ 3
avg_sales = total_sales / 3
# Target achieved = Total sales is greater than or equal to target
target_achived = "target achived" if total_sales >= target else ""
# Print the employee name and three daily sales on one line using | as the separator:
# Pratyush | 2500.0 | 3200.0 | 2800.0
print("{} | {} | {} | {}".format(employee_name,day1,day2,day3))
# Print these labeled results:
print("Total sales:",total_sales)
print("Average sales:",avg_sales)
print("Target:",target)
print("Target achieved:",target_achived)
# Use two separate print() statements to display this on one line:
# Report generated successfully
print("Report generated",end="")
print("Successfuly")