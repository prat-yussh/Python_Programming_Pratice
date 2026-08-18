# Function Q7 — Multiple Return Values

# Create a function called:

# calculate_numbers(a, b)

# It should calculate and return all three:

# Sum → a + b
# Difference → a - b
# Product → a * b

# Call it with:

# calculate_numbers(20, 5)

# Store the three returned values in:

# total, difference, product

# Then print:

# Sum: 25
# Difference: 15
# Product: 100
# Hint

# You already accidentally learned this in your create_order() question:

# return value1, value2

# This time you'll return three values.

# Give it a shot.

def calculate_numbers(a, b):
    total = a + b
    diffrence = a - b
    product = a * b

    return total,diffrence,product

total , diff , prod = calculate_numbers(20, 5)
print("Sum:",total,"\nDiffrence:",diff,"\nProduct:",prod)