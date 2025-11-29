#  Write a program which finds out whether a given name is present in a list or not. 

names=["pratyush","omm"]

user=input("Enter the name you want to find:")

if(user==names[0] or user==names[1]):
    print("The name is present in the list")
else:
    print("The name is not present in the list")

# print(names[0])