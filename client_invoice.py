# Q1: Customer Contact Masker

# Ask the user to enter:

# Customer name
# 10-digit phone number

# Example:

# Customer name: Pratyush Kumar
# Phone number: 9876543210
# Exact requirements
# Remove spaces before and after both inputs.
# Check whether the phone number contains exactly 10 characters.
# If it is not 10 characters, print:
# Invalid phone number
# Otherwise, create a masked phone number:
# ******3210

# Only the last four digits should remain visible.

# Create a customer code using:
# First 3 characters of the name in lowercase
# +
# Last 4 digits of the phone number

# For the example:

# pra3210
# Print:
# Customer: Pratyush Kumar
# Masked phone: ******3210
# Customer code: pra3210
# Short recall note
# String indexing → one character
# String slicing  → part of a string
# Strings can be joined using +

# Write the complete code yourself.

customer_name = input("Enter name:").strip()
phone_number = input("Enter phone number:").strip()

if len(phone_number) < 10:
    print("Invalid phone number")
else:
    masked_phone_number = "*" * 6 + phone_number[6:]

    customer_code = customer_name[:3] + phone_number[6:]
    print("Customer:",customer_name)
    print("Masked phone:",masked_phone_number)
    print("Customer code:",customer_code)