#  Write a program to calculate the factorial of a given number using for loop. 

num=int(input("Enter a number to find factorial:"))

factorial=1

if(num==0 or num==1):
    print("1")
else:
    for i in range(1,num+1):
        factorial=i*factorial
    print(factorial)