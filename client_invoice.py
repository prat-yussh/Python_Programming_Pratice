# Q2: Email Account Validator

# Ask the user to enter an email address.

# Example:

#   Pratyush123@Gmail.com
# Exact requirements
# Remove spaces from the beginning and end.
# Convert the complete email to lowercase.
# The email is valid only when:
# it contains exactly one @;
# @ is not the first character;
# @ is not the last character;
# the email ends with .com.
# When invalid, print:
# Invalid email
# When valid:
# extract everything before @ as the username;
# extract everything after @ as the domain.
# Print:
# Email: pratyush123@gmail.com
# Username: pratyush123
# Domain: gmail.com
# Short recall note
# count() → counts occurrences
# find() → returns the position
# endswith() → checks the ending
# slicing → extracts part of a string

email = input("Enter an email address:").lower().strip()

if email.count("@") == 1 and email.find("@") != 0 and email.rfind("@") != len(email) - 1 and email.endswith(".com") == True:
    print("Email:", email)
    print("Username:",email[:email.find("@")])
    print("Domain:",email[email.find("@")+1:])
else:
    print("Invalid email")