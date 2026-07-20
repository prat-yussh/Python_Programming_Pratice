# PDF 6 — Q3: Inventory Item Removal

# Do exactly this:

# Remove the first "Mouse" using remove().
# Remove the last item using pop().
# Store the removed last item in a variable.
# Print the updated inventory.
# Print:
# Removed last item:

# Use only remove() and pop().

inventory = ["Keyboard", "Mouse", "Monitor", "Mouse", "Webcam"]
inventory.remove("Mouse")
last_item = inventory.pop()
print(inventory)
print("Removed last item:", last_item)