"""
Write logic (no code yet)

User enters number.
Print:
"Positive Even"
"Positive Odd"
"Negative"
"Zero"
How will you structure conditions? (Think before coding.)
"""
num=int(input("Enter a number to check what type of number it is:"))

if (num>=1 and num%2==0):
    print("The number is Positive even")
elif (num>=1 and num%2!=0):
    print("The number is Positive odd")
elif (num<0):
    print("The number is a negative number")
elif (num==0):
    print("The number is Zero")