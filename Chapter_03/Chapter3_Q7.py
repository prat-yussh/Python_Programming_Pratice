"""
Fix the bug
x = input("Enter first number: ")
y = input("Enter second number: ")
print("Sum:", x + y)

Why is this wrong?
Write correct version.
"""
x = int(input("Enter first number: ")) #we need to type cast to int other wise the input always became str
y = int(input("Enter second number: "))
print("Sum:", x + y)