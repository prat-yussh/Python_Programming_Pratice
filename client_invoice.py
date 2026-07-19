# Q7: Access Code Analyzer

# A system uses codes in this format:

# A1B2C3D4
# Exact requirements
# Ask the user to enter an access code.
# Remove surrounding spaces and convert it to uppercase.
# The code is valid only when:
# it contains exactly 8 characters;
# characters at indexes 0, 2, 4, 6 are letters;
# characters at indexes 1, 3, 5, 7 are digits.
# When invalid, print:
# Invalid access code
# When valid, print:
# Valid access code: A1B2C3D4
# Letters: ABCD
# Digits: 1234
# Reversed code: 4D3C2B1A

# Use slicing with steps:

# code[::2]
# code[1::2]
# code[::-1]

# Do not use a loop. This practises the slice step and reverse slicing from the String chapter.

access_code = input("Enter the access code:").upper().strip()

if len(access_code) == 8 and access_code[::2].isalpha() and access_code[1::2].isdigit():
    print("Valid access code:",access_code)
    print("Letters:",access_code[::2])
    print("Digit:",access_code[1::2])
    print("Reversed code:",access_code[::-1])
else:
    print("Invalid access code")