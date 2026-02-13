"""
User enters a number.

Check whether it is a palindrome.

Example:
121 → Palindrome
123 → Not palindrome

Explain logic only.
"""
num=int(input("Enter a number:"))
Original_num=num
reverse=0

while num>0:
    last=num%10
    num=num//10
    reverse=reverse*10+last

if Original_num==reverse:
    print("it is a palindrome number")

else:
    print("it is not a palindrome number")