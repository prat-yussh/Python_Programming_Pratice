# PDF 6 — Q9: Filter Available Products

# This introduces list comprehension, a compact way to create a new list using a loop and condition.

# General structure:

# new_list = [value for value in old_list if condition]

# Given:

# Do exactly this:

# Create a new list named available_stock.
# Include only stock values greater than 0.
# Use one list comprehension.
# Print the new list.
# Print the number of available products.

# Expected output:

# Available stock: [12, 5, 8, 3]
# Available products: 4

# Do not use append() or a normal for loop.

product_stock = [0, 12, 5, 0, 8, 3]
available_stock = [value for value in product_stock if value > 0]
print(available_stock)
print(len(available_stock))