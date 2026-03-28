"""
Count Each Character

User enters a string.
Count how many times each character appears.

Example
Input
AABBC

Output
A → 2
B → 2
C → 1
"""
text=input("Enter a string:")
for i in set(text):
    print("{}:{}".format(i, text.count(i)))