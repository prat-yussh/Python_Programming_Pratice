# Q2: Delivery Queue Update

# Do exactly this:

# Add "Order-104" at the end using append().
# An urgent order "Order-999" must be placed at index 1 using insert().
# Print the updated queue.
# Print the total number of orders.

# Expected list:

# ['Order-101', 'Order-999', 'Order-102', 'Order-103', 'Order-104']

# Use only:

# append()
# insert()
# len()

# append() adds at the end, while insert() adds at a specified index.

delivery_queue = ["Order-101", "Order-102", "Order-103"]

delivery_queue.append("Order-104")
delivery_queue.insert(1,"Order-999")
print(delivery_queue)
print("Total number of orders:",len(delivery_queue))