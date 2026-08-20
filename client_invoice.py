# Modules Q3 — Alias with as

# Sometimes module/function names are long, so Python lets us give them a shorter name.

# For example:

# import math as m

# Then:

# m.sqrt(25)

# instead of:

# math.sqrt(25)
# Your task

# Use the random module.

# Import random as r.

# Generate a random integer between 1 and 100 using:

# r.randint(1, 100)
# Store it in number.

# Print:

# Random number: <number>
# Hint
# import random as r

# Then use:

# r.randint(...)

# That's it—one small question, then we'll move to creating your own module, which is the important part.

import random as r

print(r.randint(1,100))