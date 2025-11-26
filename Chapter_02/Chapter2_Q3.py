# Check the type of variable assigned using input () function.

a=type(input("Enter your name:"))
b=type(int(input("Enter a Number:")))
c=type(float(input("Enter a Decimal Number:")))
d=type(bool(input("Your a boy answer me with Yes or No:")))

print(a)
print(b)
print(c)
print(d)