"""
Palindrome String
User enters a string.

Check whether it is a palindrome.

Example
madam → Palindrome
hello → Not Palindrome
"""

mainString = input("Enter a string: ")

reverse=""

for ch in mainString:
    reverse=ch+reverse

print(reverse)

if mainString==reverse:
    print("Palindrome")
else:
    print("Not Palindrome")