# Q5: Employee employee_id Valemployee_idator

# Ask the user to enter an employee employee_id.

# Valemployee_id format:

# ABC1234
# Exact requirements

# The employee employee_id is valemployee_id only when:

# it contains exactly 7 characters;
# the first 3 characters are alphabets only;
# the last 4 characters are digits only.

# Convert the first three letters to uppercase before printing.

# Example 1
# Input: abc1234
# Valemployee_id employee employee_id: ABC1234
# Example 2
# Input: ab12345
# Invalemployee_id employee employee_id

# Use:

# len()
# slicing
# isalpha()
# isdigit()
# upper()

# Do not use a loop.

employee_id = input("enter an employee employee_id:").upper()

if len(employee_id) == 7 and employee_id[:3].isalpha() == True and employee_id[-4:].isdigit() == True:
    print("Valemployee_id employee employee_id:",employee_id)
else:
    print("Invalemployee_id employee_id:")