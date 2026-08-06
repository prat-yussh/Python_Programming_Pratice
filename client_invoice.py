# Q4: Merge Visitor Sets

# Do exactly this:

# Create a new set named all_visitors using union().
# Print all_visitors.
# Print the total number of unique visitors.
# Expected result
# {'V101', 'V102', 'V103', 'V104', 'V105'}
# Total visitors: 5

# Use only:

# union()
# len()

# Do not use a loop.

# Hint: union() combines both sets and automatically removes duplicates.

morning_visitors = {"V101", "V102", "V103"}
evening_visitors = {"V103", "V104", "V105"}

all_visitors = morning_visitors.union(evening_visitors)
print(all_visitors)
print(len(all_visitors))