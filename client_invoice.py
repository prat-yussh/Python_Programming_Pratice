# Q5: Common Customers

# Do exactly this:

# Find the customers who visited both stores using intersection().
# Store the result in common_customers.
# Print common_customers.
# Print the number of common customers.

# Use only:

# intersection()
# len()

# Do not use a loop.

# This introduces another important set operation:

# union() → all unique elements
# intersection() → only common elements

store_a = {"Asha", "Rahul", "Pratyush", "Riya"}
store_b = {"Rahul", "Riya", "Aman"}

common_customers = store_a.intersection(store_b)
print(common_customers)
print(len(common_customers))