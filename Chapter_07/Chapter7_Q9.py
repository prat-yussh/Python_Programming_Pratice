"""
Write a program to print the following star pattern. 
* * * 
*   *   for n = 3 
* * * 
"""

n=int(input("Enter a number:"))

for i in range(1,n+1):
    print("*"*(n))
    print("*",end="")
    print("")

    # for j in range(2):
    #     print("*")
    #     if(i==2):
        
    # print("*")
