# Q12: Create Stock Statuses

# Create a new list named stock_status.

# For each value:

# If the stock is 0, add "Out of stock".
# Otherwise, add "Available".

# Expected result:

# Stock status: ['Out of stock', 'Available', 'Available', 'Out of stock', 'Available']

# Use one list comprehension with if-else.

# Structure:

# [value_if_true if condition else value_if_false for item in list_name]

# Do not use a normal loop or append().

product_stock = [0, 12, 5, 0, 8]

stock_status = ["Available" if product == 0 else "Out of stock" for product in product_stock]
print(stock_status)