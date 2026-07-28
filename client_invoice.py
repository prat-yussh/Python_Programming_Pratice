# Q6: Analyze Fixed Delivery Times

# Do exactly this:

# Print the shortest delivery time using min().
# Print the longest delivery time using max().
# Sort the tuple in ascending order using sorted().
# Store the result in sorted_times.
# Print sorted_times.
# Print the type of sorted_times.
# Print the original delivery_times to confirm it remains unchanged.

# Important:

# sorted(tuple_name)

# returns a list, not a tuple, because the original tuple cannot be modified.

# Expected main results:

# Shortest time: 28
# Longest time: 50
# Sorted times: [28, 35, 40, 42, 50]
# Type: <class 'list'>

delivery_times = (42, 35, 50, 28, 40)

sorted_times = sorted(delivery_times)

print("Shortest time:",min(delivery_times))
print("Longest time:",max(delivery_times))
print("Sorted times:",sorted_times)
print("Type",type(sorted_times))
