# Write a program to find whether a given username contains less than 10 characters or not. 

username=input("Enter your username:")

number_of_character=len(username)

if(number_of_character>10):
    print("thid username is valid and its contains more than 10 or more charcter in the username ")
else:
    print("thid username is not valid and its doesnt contains more than 10 or more charcter in the username ")