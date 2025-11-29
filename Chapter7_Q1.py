# Write a program to print multiplication table of a given number using for loop. 

i=1

num=int((input("Enter the number to print multiplication table:")))

for i in range(11):
    print(f"{num}X{i}={num*i}")