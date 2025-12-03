"""
Write a python function to print first n lines of the following pattern: 
*** 
**               
*
"""

def display(n):
    if(n==0):
        return
    print("*"*n)
    display(n-1)

n=int(input("Enter a number:"))
display(n)