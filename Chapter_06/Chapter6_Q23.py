"""
User enters a number.

Count how many digits it has.

(No using len(str(n)) — think mathematically.)
"""
num=int(input("Enter a number:"))

if num<0:
    num= -num

if num==0:
    count=1
   
else:
    count=0
    while num>0:
        num = num//10
        count=count+1

print("Number of digits are:{}".format(count))