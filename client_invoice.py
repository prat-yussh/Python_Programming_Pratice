# Function Q8 — *args

# Now we're moving to a new concept.

# Create:

# calculate_total(*prices)

# The function should accept any number of prices and return their total.

# For example:

# calculate_total(100, 200, 300)

# should return:

# 600

# And:

# calculate_total(50, 100, 150, 200)

# should return:

# 500
# Requirements

# Inside the function:

# Start total = 0
# Loop through prices
# Add each price to total
# Return total

# Then test:

# print(calculate_total(100, 200, 300))
# print(calculate_total(50, 100, 150, 200))
# New concept
# def calculate_total(*prices):

# *prices means the function can receive any number of positional arguments.

# Don't worry about **kwargs yet. One new concept at a time.

def calculate_total(*prices):
    start_total = 0
    for price in prices:
        start_total = start_total + price

    return start_total

print(calculate_total(100, 200, 300))
print(calculate_total(50, 100, 150, 200))