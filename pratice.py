# Q4: Trusted Expense Calculator

# A freelancer wants a tiny calculator for checking an expense formula.

# Input

# Ask the user to enter one arithmetic expression.

# Example:

# Enter calculation: 1200 + 850 * 3
# Program requirements
# Store the entered expression in calculation.
# Evaluate the expression and store the answer in result.
# Print:
# ------ CALCULATION ------
# Expression: 1200 + 850 * 3
# Result: 3750
# Result type: <class 'int'>
# -------------------------
# Test your program once with:
# 1500 + 900 + 300
# Test it again with:
# 5000 / 4

result = eval(input("Expression"))
print("------ CALCULATION ------")
# print("Expression:",calculate)
print("Result:",result)
print("Result type:",type(result))
print("-------------------------")