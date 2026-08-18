# Function Q4 — Keyword Arguments + Multiple Parameters

# Create a function called create_order with these parameters:

# product
# quantity
# price

# The function should:

# Calculate the total:
# quantity × price
# Return the total.

# Then call the function using keyword arguments, not positional arguments.

# Use:

# product = "Keyboard"
# quantity = 2
# price = 1200

# Your call should look like the idea below:

# create_order(
#     product="Keyboard",
#     quantity=2,
#     price=1200
# )

# Store the returned value in total and print:

# Product: Keyboard
# Total: 2400

# Don't use input() or loops.

def create_order(product,quantity,price):
    total_price = price * quantity
    return product,total_price

product, total = create_order(
    product="Keyboard",
    quantity=2,
    price=1200
)

print("prodct:",product,"\nTotal:",total)