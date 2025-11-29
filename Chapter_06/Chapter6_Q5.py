#  Write a program which finds out whether a given name is present in a list or not. 

names=["pratyush","omm","kakasi","naruto","harry"]

user=input("Enter the name you want to find:")

if(user in names):
    print("The name is present in the list")
else:
    print("The name is not present in the list")