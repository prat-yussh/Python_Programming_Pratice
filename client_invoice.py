# Function Q2 — Multiple Calculations + Return

# Create a function called calculate_bill that takes:

# price
# quantity
# discount

# The function should:

# Calculate the original bill:
# price × quantity
# Calculate the discount amount:
# bill × discount / 100
# Calculate the final bill:
# bill - discount_amount
# Return the final bill.

# Then call:

# calculate_bill(1000, 3, 10)

# Store the result in final_bill and print it.

# Expected result:

# Final bill: 2700.0

# Don't use input() or loops. Just focus on parameters, calculations, and return.

def calculate_bill(price,quantity,discount):
    original_bill = price * quantity
    discount_amount = original_bill * discount / 100
    final_bill = original_bill - discount_amount
    return final_bill

final_bill = calculate_bill(1000,3,10)
print("Final bill:",final_bill)