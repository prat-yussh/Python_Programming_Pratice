"""
User enters a number.

Check if it is a prime number.

Explain your full thinking process.
"""

num=int(input("Enter a number:"))

is_prime=True

if num<0:
    is_prime=False

else:
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
        
if is_prime:
    print("its is a prime number")
else:
    print("its is not a prime number")
