"""
x = 5
if x == 5 or 10:
    print("Hello")
Will it always print Hello? Why?
"""

x = 5
if x == 5 or 10: #It always prints "Hello" because 10 is a truthy value, even if x==0 it will print "Hello".
    print("Hello")