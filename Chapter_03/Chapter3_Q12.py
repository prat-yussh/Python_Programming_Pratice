"""
String Length Logic
User enters a string.
Print whether the string length is:

Even
Odd

Example
Hello → Odd
Python → Even
"""

text=input("Enter a string to check its even or odd:")

length=len(text)

print("Even" if length % 2 == 0 else "Odd")