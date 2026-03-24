"""
Count a Character
User enters:
a string
a character

Count how many times the character appears.

Example
Input

String: banana
Character: a

Output
3
"""

text=input("Enter a string:")
charcter=input("Enter a character to find how many time it is used in the string:")

repeat=text.count(charcter)

print("String: {} \nCharacter: {}\nRepeated:{}".format(text,charcter,repeat))