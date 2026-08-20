# Modules Q2 — from ... import ...

# Instead of:

# import math


# math.sqrt(25)

# Python also lets you import specific functions:

# from math import sqrt

# Then you can directly write:

# sqrt(25)
# Your task

# Write a program that:

# Imports sqrt and ceil from math.

# Use:

# Find the square root.
# Round the number up using ceil().
# Print both.

# Expected roughly:

# Square root: 2.701...
# Rounded up: 8

# Use:

# from math import ...

# instead of import math.

from math import sqrt,ceil

number = 7.3
print(sqrt(number))
print(ceil(number))