# Dictionary Q3 (Combined)

# Do all of these:

# Remove "Monitor" using pop().
# Store the removed value in a variable named removed_stock.
# Print:
# Removed stock: 5
# Increase "Keyboard" stock by 5.
# Add:
# "Speaker": 10
# Print the updated dictionary.
# Print the total number of products.

# This single question practices:

# pop()
# Updating an existing value
# Adding a new key
# len()

# This is very close to how dictionaries are used in inventory systems.

inventory = {
    "Mouse": 15,
    "Keyboard": 8,
    "Monitor": 5,
    "Webcam": 12
}

removed_stock = inventory.pop("Monitor")
print(removed_stock)
print(inventory)

inventory["Keyboard"] += 5
inventory["Speaker"] = 10

print(inventory)
print(len(inventory))