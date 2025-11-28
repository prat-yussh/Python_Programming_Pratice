#  Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique. 

database={}

name=input("enter your name:")
subject=input("enter your fav subject:")

database.update({name:subject})
name=input("enter your name:")
subject=input("enter your fav subject:")

database.update({name:subject})
name=input("enter your name:")
subject=input("enter your fav subject:")

database.update({name:subject})
name=input("enter your name:")
subject=input("enter your fav subject:")

database.update({name:subject})

print(database)
