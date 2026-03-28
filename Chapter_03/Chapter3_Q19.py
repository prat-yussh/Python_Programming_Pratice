"""
Print Characters at Even Position
User enters a string.

Print characters at:
even index
odd index

Example
Python

Output
Even index: P t o
Odd index: y h n
"""
text=input("Enter a string:")

print("Even Index:", end="")
for i in range(0, len(text)):
    if i%2==0:
        print(text[i], end=" ")

print("\nOdd Index:", end="")
for i in range(0, len(text)):
    if i%2!=0:
        print(text[i], end=" ")