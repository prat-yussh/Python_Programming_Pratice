# Q8: Check Customer Membership

# Do exactly this:

# Ask the user to enter a customer name.
# If the customer is in premium_customers, print:
# Premium customer

# Otherwise print:

# Regular customer

# Use only:

# input()
# in
# if...else

# Do not use a loop.

premium_customers = {"Asha", "Rahul", "Pratyush"}
name = input("Enter a customer name:")

if name in premium_customers:
    print("Premium customers")
else:
    print("Regular customers")
