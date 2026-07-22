# PDF 6 — Q10: Apply Product Discount

# Create a new list named discounted_prices.

# Each price receives a 10% discount:


# Expected result:

# Discounted prices: [450.0, 1080.0, 720.0, 1800.0]

# Requirements:

# Use one list comprehension.
# Do not modify prices.
# Do not use a normal loop or append().
# Print both the original and discounted lists.

prices = [500, 1200, 800, 2000]

discounted_prices = [
    price - (price * 10 / 100)
    for price in prices
]

print("Original prices:", prices)
print("Discounted prices:", discounted_prices)