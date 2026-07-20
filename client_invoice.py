# Q5: Product Search and Count

# Do exactly this:

# Print how many times "Mouse" appears using count().
# Print the index of the first "Monitor" using index().
# Check whether "Webcam" exists in the list.
# Print either:
# Webcam available

# or:

# Webcam not available

# Do not use a loop.

products = ["Mouse", "Keyboard", "Mouse", "Monitor", "Mouse"]

print("Mouse counts:",products.count("Mouse"))
print("Mouse counts:",products.index("Monitor"))

item = "Webcam" 

if item in products:
    print("Webcam available")
else:
    print("Webcam not available")
