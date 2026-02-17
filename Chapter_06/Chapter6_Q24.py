"""
User enters a number.

Reverse the number.

Example:
Input: 1234
Output: 4321

Explain your step-by-step thinking.
"""
num=int(input("Enter a number:"))
original_num=num
reverse=0

while num>0:
    last=num%10
    num=num//10
    reverse=reverse*10+last

print(reverse)