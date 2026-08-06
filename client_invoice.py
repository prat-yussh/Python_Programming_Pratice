# Q3: Safe Product Removal

# Do exactly this:

# Remove "Keyboard" using discard().
# Try to remove "Webcam" using discard().
# Print the final set.
# Print the total number of products.
# New concept

# discard() is safer than remove().

# products.remove("Webcam")   # ❌ Error if Webcam doesn't exist

# products.discard("Webcam")  # ✅ No error, nothing happens

# Use:

# discard()
# len()

# Do not use a loop.

# This question teaches the difference between remove() and discard(), which is one of the most important set methods.

products = {"Mouse", "Keyboard", "Monitor"}
products.discard("Keyboard")
products.discard("Webcam")
print(products)
print(len(products))