# Write a program to find whether a given number is prime or not.

num=int(input("Enter the number to check the number is prime or not:"))

prime=0

for i in range(100):
    if(num%1==0 and num%2==0):
        print("the number is prime")
    else:
        print("the number is not prime")
