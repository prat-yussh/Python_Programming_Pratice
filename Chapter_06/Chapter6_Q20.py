"""
User enters a number.

Print:
"Divisible by 3"
"Divisible by 5"
"Divisible by both"
"Not divisible by either"

How will you structure conditions?
(Think about order carefully.)
"""
num=int(input("Enter a number:"))

if num%3==0 and num%5==0:
    print("the number is divisble by both 3 and 5.")
    
elif num%3==0:
    print("the number is divisble by 3.")

elif num%5==0:
    print("the number is divisble by 5.")

else:
    print("the number is not divisble by 3 and 5.")