# Q7: Employee Salary Slip

# Take these values from the keyboard:

employee_name = input("Enter your name:")
basic_salary = float(input("Enter your salary:"))
Allowance = float(input("Enter your allowence:"))
Deduction = float(input("Enter your deduction:"))
# Calculate
gross_salary = basic_salary + Allowance

Net_salary = gross_salary - Deduction
# Print this exact report
print("-------- SALARY SLIP --------")
print("Employee:{}".format(employee_name))
print("Basic salary:{:.2f}".format(basic_salary))
print("Allowance:{:.2f}".format(Allowance))
print("Deduction:{:.2f}".format(Deduction))
print("Gross salary:{:.2f}".format(gross_salary))
print("Net salary:{:.2f}".format(Net_salary))
print("-----------------------------")
# Exact requirements
# Employee name remains a string.
# All money values must be converted to float.
# Show every money value with exactly two decimal places.
# Use .format() for the salary output lines.
# Do not hardcode the values.