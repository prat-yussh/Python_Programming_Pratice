# Write a program using functions to find greatest of three numbers. 

def compare(a,b,c):
    if(a>b and a>c):
        print("1st number is greatest")
    elif(b>a and b>c):
        print("2nd number is greatest")
    elif(c>a and c>b):
        print("3rd number is greatest")

compare(6,5,20)