# Q6: Customer Name Formatter

# Example input:

#   pRATYUSH   kumar

# Expected output:

# Name corrected
# Formatted name: Pratyush Kumar
# Requirements
# Remove spaces from both ends.
# Remove extra spaces between words using split() and join().
# The name is valid only when it contains letters and spaces.
# If invalid, print:
# Invalid name
# If the cleaned name is already in title case, print:
# Name already formatted
# Otherwise, print:
# Name corrected
# Print the name in title case.

# Use:

# strip()
# split()
# join()
# replace()
# isalpha()
# istitle()
# title()

# istitle() checks the current format, while title() returns a title-cased string.
name = input("Enter your name: ").strip()
cleaned_name = " ".join(name.split())

if not cleaned_name.replace(" ", "").isalpha():
    print("Invalid name")

elif cleaned_name.istitle():
    print("Name already formatted")
    print("Formatted name:", cleaned_name)

else:
    print("Name corrected")
    print("Formatted name:", cleaned_name.title())