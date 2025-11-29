"""
Write a program to greet all the person names stored in a list "l" and which starts with S. 
l = ["Harry", "Soham", "Sachin", "Rahul"]
"""

l = ["Harry", "Soham", "Sachin", "Rahul"]

greet="have a nice day"

for i in l:
    if(i.startswith("S")):
        print(f"{greet} {i}")