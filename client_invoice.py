# Function Q1 — Basic Function + Parameter + Return

# Write a function called calculate_total that:

# Takes two parameters:
# price
# quantity
# Calculates:
# price × quantity
# Returns the total.

# Then:

# Call the function with 500 and 3.
# Store the returned result in a variable called total.
# Print:
# Total price: 1500
# Example idea

# You'll need:

# def function_name(...):
#     ...
#     return ...

# Don't worry about formatting the output exactly yet. Focus on getting the function + parameters + return + function call correct.

def calculate_total(price,quantity):
    return price * quantity

total = calculate_total(500,3)
print("Total price:",total)