"""
Write a python function to print first n lines of the following pattern: 
*** 
**               
*
"""

def display(n):
    for i in range(1,n+1):
        print("*",end="")
        print("*",end="")
n=int(input("Enter a number"))
display(n)

# i=1 ****
# i=2 ***
# i=3 **
# i=4 *