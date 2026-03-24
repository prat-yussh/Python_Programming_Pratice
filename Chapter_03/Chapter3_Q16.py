"""
Reverse a String (Without slicing)

User enters a string.

Reverse it using logic only.

Example
Python

Output
nohtyP
"""

mainString = input("Enter a string: ")

reverse = ""

for ch in mainString:
    reverse = ch + reverse

print(reverse)