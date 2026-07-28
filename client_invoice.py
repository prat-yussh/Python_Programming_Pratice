# Final Question: Available Inventory

# The product and its stock share the same index:

# Mouse → 5
# Keyboard → 0
# Monitor → 3
# Webcam → 0

# Create a list named available_products containing only products whose stock is greater than 0.

# Expected output:

# Available products: ['Mouse', 'Monitor']
# Available product count: 2

# Use one list comprehension with indexes:

# products[i] for i in range(len(products))

# Do not use a normal loop or append().

products = ["Mouse", "Keyboard", "Monitor", "Webcam"]
stock = [5, 0, 3, 0]

available_products = [products[i] for i in range(len(products)) if stock[i] > 0]
print("Available products:",available_products)
print("Available product count:",len(available_products))