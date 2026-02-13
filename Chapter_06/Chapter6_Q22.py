"""
User enters a number n.

Print:
Sum of all even numbers from 1 to n.

Explain your logic steps only.
"""
num=int(input("Enter a number:"))

sum=0

for i in range(1,num):
    if i%2==0:
        sum=sum+i
    
print("Sum of all even numbers from 1 to n:{}".format(sum))