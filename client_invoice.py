# Q7: Employee Record Packing and Unpacking

# Do exactly this:

# Pack all three variables into a tuple named employee_record without writing the values again.
# Print employee_record.
# Print its type.
# Unpack it into:
# saved_id, saved_name, saved_department
# Print all three unpacked variables.

# Expected tuple:

# ('EMP-101', 'Asha', 'IT')

# Remember:

# employee_record = employee_id, employee_name, department  # packing

# saved_id, saved_name, saved_department = employee_record  # unpacking

# During unpacking, the number of variables must equal the number of tuple values.

employee_id = "EMP-101"
employee_name = "Asha"
department = "IT"

employee_record = employee_id, employee_name, department
print(employee_record)
saved_id, saved_name, saved_department = employee_record

print(saved_id)
print(saved_name)
print(saved_department)