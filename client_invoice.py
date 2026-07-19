# Q8: Password Character Analyzer

# Ask the user to enter a password.

# Exact requirements

# Check every character and manually count:

# uppercase letters
# lowercase letters
# digits
# spaces

# The password is valid only when:

# its length is at least 8;
# it contains at least one uppercase letter;
# it contains at least one lowercase letter;
# it contains at least one digit;
# it contains no spaces.
# Example
# Input: Python123

# Uppercase letters: 1
# Lowercase letters: 5
# Digits: 3
# Spaces: 0
# Valid password

# Otherwise print:

# Invalid password

# Use one for loop with:

# isupper()
# islower()
# isdigit()
# isspace()

# Do not use count(). These character-checking methods are covered in the String chapter.

password = input("Enter your password:")
upper_case = 0
lower_case = 0
digit = 0
spaces = 0

for i in password:
    if i.isupper():
        upper_case += 1
        
        
    elif i.islower():
        lower_case += 1
        
        
    elif i.isnumeric():
        digit += 1
        
        
    elif i.isspace():
        spaces += 1
        
        

if len(password) >= 8 and upper_case >= 1 and lower_case >= 1 and spaces == 0 and digit >= 1:
    print("Uppercase letters:",upper_case)
    print("Lowercase letters:",lower_case)
    print("Digits:",digit)
    print("Spaces:",spaces)
    print("Valid password")
else:
    print("Invalid password")