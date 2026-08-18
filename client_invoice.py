# Function chapter: one final challenge 🔥

# This will combine almost everything we've learned.

# Create:

# generate_bill(customer, *prices, discount=10)

# The function should:

# Accept the customer's name.
# Accept any number of prices using *prices.
# Calculate the total of all prices.
# Apply the discount.
# Return customer name + final bill.

# Call:

# generate_bill("Pratyush", 500, 1200, 800, discount=10)

# Expected:

# Customer: Pratyush
# Final bill: 2250.0
# Why 2250?
# 500 + 1200 + 800 = 2500
# 10% discount = 250
# Final = 2250

# Important: Don't use sum().

# This is the final function challenge. After this, Functions = DONE and we move to the next Python topic. 🚀

def generate_bill(customer, *prices, discount=10):
    total = 0
    for price in prices:
        total += price

    discount = total * discount / 100
    final_price = total - discount
    return customer, final_price

customer, final_price = generate_bill(
    "Pratyush", 500, 1200, 800, discount=10
)

print("Customer:", customer)
print("Final bill:", final_price)