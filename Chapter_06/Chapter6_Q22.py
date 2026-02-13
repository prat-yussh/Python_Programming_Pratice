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
"""
here are the logic steps

step-1:user takes input and create a "sum" varriable
step-2:A loop starts from 1 to user entered "num"
step-3:If condition starts and checks the number is even or not
step-4:if condition satisfied the add to "sum" varriable
"""