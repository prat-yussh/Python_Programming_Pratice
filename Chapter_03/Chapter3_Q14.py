"""
Membership Check
User enters:
main string
substring

Print:
Substring Found

or

Substring Not Found

(Use logic thinking.)
"""

text=input("Enter a string:")
subText=input("Enter a sub string:")

if subText in text:
    print("Substring Found")
else:
    print("Substring Not Found")
