# Q2: Single-Value Tuple

# A system stores one fixed administrator ID:

# ADMIN-101

# Create a tuple named admin_record containing only this one value.

# Then print:

# Admin record:
# Length:
# Type:
# Important new rule

# A single-value tuple must contain a comma:

# value = ("ADMIN-101",)

# Without the comma:

# value = ("ADMIN-101")

# Python treats it as a normal string, not a tuple.

# Write the complete code.

admin_record = ("ADMIN-101",)

print(len(admin_record))
print(type(admin_record))