# Function Q5 — Function + Condition

# Now let's combine functions with the if logic you've been practicing.

# Create:

# check_discount(price)

# The function should:

# If price >= 1000, return "10% discount available"
# Otherwise, return "No discount available"

# Then call it with:

# 1200

# and:

# 800

# Expected:

# 10% discount available
# No discount available

# Use return, not print() inside the function.
def check_discount(price):
    if price >= 1000:
        return "10 \% discount available"
    else:
        return "No discount available"

result = check_discount(1000)
print(result)