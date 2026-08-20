# Modules Q4 — Create Your Own Module

# This is more important because you'll use this concept in real projects.

# Create two Python files in the same folder:

# File 1: calculator.py

# Create these two functions:

# add(a, b)
# multiply(a, b)
# add() should return a + b
# multiply() should return a * b
# File 2: main.py

# Import your calculator module:


# Then:

# Call calculator.add(10, 5)
# Call calculator.multiply(10, 5)
# Print both results.

# Expected:

# Addition: 15
# Multiplication: 50
# Think of it like this
# calculator.py
#       ↓
# contains reusable functions
#       ↓
# main.py
#       ↓
# imports and uses them

# This is how larger Python projects are organized instead of putting everything into one giant .py file.

# Create the two files and try it.

import calculator

print("Addition:",calculator.add(10, 5))
print("Multilpicartion:",calculator.multiply(10, 5))