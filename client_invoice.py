# Q7: Customers Visiting Only One Store

# Do exactly this:

# Find customers who visited only one of the stores using symmetric_difference().
# Store the result in unique_customers.
# Print unique_customers.
# Print the total number of unique customers.

# Use only:

# symmetric_difference()
# len()

# Do not use a loop.

# 💡 Before coding, think:

# Rahul visited both stores → Should he appear?
# Asha visited only Store A → Should she appear?
# Aman visited only Store B → Should he appear?

store_a = {"Asha", "Rahul", "Pratyush", "Riya"}
store_b = {"Rahul", "Riya", "Aman"}

unique_customers = store_a.symmetric_difference(store_b)
print(unique_customers)
print(len(unique_customers))