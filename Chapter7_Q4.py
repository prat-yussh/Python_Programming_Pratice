# Write a program to find whether a given number is prime or not.

num=int(input("Enter the number to check the number is prime or not:"))

i=2

for i in range(i,num):
    if(num%i==0):
        print("the number is not prime.")
        break
else:
    print("the number is prime.")