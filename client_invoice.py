# Q13: Filter and Discount Expensive Products

# Create a new list named discounted_expensive_prices.

# Rules:

# Select only prices greater than or equal to 1000.
# Give those selected prices a 10% discount.
# Do not include prices below 1000.

# Formula:

# Discounted price = price - (price × 10 / 100)

# Expected output:

# Discounted expensive prices: [1080.0, 1800.0, 1350.0]

# Use one list comprehension:

# [expression for item in list_name if condition]
# Do not use a normal loop or append(). This combines transformation and filtering.

prices = [500, 1200, 800, 2000, 1500]
discounted_expensive_prices = [item - (item * 10 / 100) for item in prices if item >= 1000]

print(discounted_expensive_prices)