"""
Example:
145

1! + 4! + 5! = 145

You'll need factorial logic inside digit loop.

How will you structure nested logic?
"""

num=int(input("Enter a number:"))

digit=0
while num>0:
    num=num//10
    digit=digit+1

print(digit)