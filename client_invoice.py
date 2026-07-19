# Q9: Username Order Checker

# A website wants to arrange two usernames alphabetically.

# Ask the user to enter two usernames.

# Exact requirements
# Remove spaces from both ends.
# Convert both usernames to lowercase.
# If either username is empty, print:
# Invalid username
# If both usernames are the same, print:
# Both usernames are identical
# Otherwise, compare them using <.

# Example:

# First username: Pratyush
# Second username: Rahul

# Output:

# Alphabetical order:
# pratyush
# rahul

# Another example:

# First username: Zoya
# Second username: Amit

# Output:

# Alphabetical order:
# amit
# zoya

# Use if/elif/else and string comparison. Python compares strings alphabetically character by character.

username_1 = input("Enter first username: ").strip().lower()
username_2 = input("Enter second username: ").strip().lower()

if not username_1 or not username_2:
    print("Invalid username")

elif username_1 == username_2:
    print("Both usernames are identical")

elif username_1 < username_2:
    print("Alphabetical order:")
    print(username_1)
    print(username_2)

else:
    print("Alphabetical order:")
    print(username_2)
    print(username_1)