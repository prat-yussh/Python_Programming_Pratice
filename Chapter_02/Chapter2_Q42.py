"""
Identity + Mutability Trap
a = [1, 2, 3]
b = a
c = a[:]

print(a is b)
print(a is c)
print(a == c)
"""
a = [1, 2, 3]
b = a
c = a[:]

print(a is b) #True
print(a is c) #False
print(a == c) #TRue