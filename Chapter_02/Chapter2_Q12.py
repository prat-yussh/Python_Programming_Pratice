"""
Identity vs Equality
a = [1, 2]
b = [1, 2]
print(a == b)
print(a is b)
"""

a = [1, 2]
b = [1, 2]
print(a == b) #True because "==" is used for content comparision 
print(a is b) #False because "is" used for refrence comparision and checks memory adress and a and b is stored in diffrent address