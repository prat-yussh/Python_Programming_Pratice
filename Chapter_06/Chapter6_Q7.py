# Write a program to find out whether a given post is talking about “Harry” or not.

name="Harry"

post=input("Enter the post to check whether a given post is talking about “Harry” or not:")

if(name.lower() in post.lower()):
    print("The given post is talking about harry.")
else:
    print("The given post is not talking about harry.")
