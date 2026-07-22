# Q11: Find Common Products

# Create a new list named common_products containing only products present in both lists.

# Expected output:

# Common products: ['Monitor', 'Webcam']
# Number of common products: 2

# Requirements:

# Use one list comprehension.
# Use the in operator inside it.
# Do not use a normal loop or append().
# Do not modify either original list.

# Structure to remember:

# [value for value in first_list if value in second_list]

# This type of common-element filtering is included in the List chapter.

store_a = ["Mouse", "Keyboard", "Monitor", "Webcam"]
store_b = ["Monitor", "Webcam", "Printer"]

common_products = [store_a for store_b in store_a if store_a in store_b]