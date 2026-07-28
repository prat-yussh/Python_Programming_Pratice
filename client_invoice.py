# Q5: Update a Fixed Permission Record

# The last permission must be changed from "Download" to "Upload".

# Do exactly this:

# Print the original tuple.
# Convert the tuple into a list using list().
# Change the value at index 2 to "Upload".
# Convert the list back into a tuple using tuple().
# Print the updated tuple.
# Print its data type.

# Expected result:

# Original permissions: ('Read', 'Write', 'Download')
# Updated permissions: ('Read', 'Write', 'Upload')
# Type: <class 'tuple'>

# Do not create the updated tuple manually.

permissions = ("Read", "Write", "Download")

print("Original permissions:", permissions)

permissions = list(permissions)
permissions[2] = "Upload"
permissions = tuple(permissions)

print("Updated permissions:", permissions)
print("Type:", type(permissions))