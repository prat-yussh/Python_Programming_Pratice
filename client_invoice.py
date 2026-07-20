# PDF 6 — Q4: Merge Delivery Batches

# Do exactly this:

# Add all items from evening_orders to morning_orders using extend().
# Print the combined order list.
# Print the total number of orders using len().
# Print evening_orders to confirm that it remains unchanged.

# Expected combined list:

# ['Order-201', 'Order-202', 'Order-203', 'Order-204', 'Order-205']

# Do not use a loop, +, or repeated append().

# extend() adds each element of one collection to another list.

morning_orders = ["Order-201", "Order-202"]
evening_orders = ["Order-203", "Order-204", "Order-205"]

morning_orders.extend(evening_orders)
print("All orders:",morning_orders)
print("Total number of orders:",len(evening_orders))
print("Evening orders:",evening_orders)
