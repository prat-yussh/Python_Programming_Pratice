# Q4: Product URL Generator

# An online shop needs to convert a product name into a clean URL name.

# Example input:

#   Wireless   Mouse / Gaming  

# Expected output:

# Product URL: wireless-mouse-gaming
# Exact requirements
# Ask the user to enter a product name.
# Remove spaces from the beginning and end.
# Convert it to lowercase.
# Replace / with a space.
# Use split() so extra spaces are removed.
# Join the words using -.
# Print the final product URL.

# For another example:

# Input:  Apple   MacBook Pro
# Output: apple-macbook-pro

# Use replace(), split(), and join().

url = input("Enter product name:").lower().strip()
url = url.replace("/"," ")
words = url.split()
url = "-".join(words)
print("Product URL:", url)