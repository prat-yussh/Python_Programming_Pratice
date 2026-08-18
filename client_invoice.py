# Function Q9 — *args + Condition

# Let's make this one more practical.

# Create a function:

# calculate_expensive_total(*prices)

# It should:

# Accept any number of prices.
# Look at each price.
# Add only prices greater than or equal to ₹1000.
# Return the total.

# Example:

# calculate_expensive_total(500, 1200, 800, 2000)

# Expected:

# 3200

# Because:

# 500  ❌
# 1200 ✅
# 800  ❌
# 2000 ✅


# 1200 + 2000 = 3200

# Test it with:

# print(calculate_expensive_total(500, 1200, 800, 2000))
# print(calculate_expensive_total(1500, 700, 2500))

# Expected:

# 3200
# 4000
# Rules

# Use:

# *args
# for
# if
# return

# No sum().

# This is basically the *args question you just learned + the filtering logic you've already practiced.

def calculate_expensive_total(*prices):
    total = 0
    for price in prices:
        if price >= 1000:
            total = total + price
        else:
            pass

    return total



print(calculate_expensive_total(500, 1200, 800, 2000))
print(calculate_expensive_total(1500, 700, 2500))