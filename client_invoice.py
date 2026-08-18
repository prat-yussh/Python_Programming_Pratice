# Task

# Create:

# calculate_final_price(price, discount=10)

# Rules:

# If price >= 1000 → apply the discount.
# If price < 1000 → no discount.
# Return the final price.

# Test these:

# calculate_final_price(2000)
# calculate_final_price(2000, 20)
# calculate_final_price(800)

# Expected:

# 1800.0
# 1600.0
# 800
# Concepts being tested
# def
# parameters
# default parameter
# if/else
# calculation
# return
# function calls

# Give it a try yourself. Don't overthink it—you've already used every piece of this.

def calculate_final_price(price, discount=10):
    if price >= 1000:
        discount_amount = price * discount / 100
        total_amount = price - discount_amount
        return total_amount
    else:
        return price

print(calculate_final_price(2000))
print(calculate_final_price(2000, 20))
print(calculate_final_price(800))