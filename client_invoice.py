# Dictionary Final Challenge

# You have an online store:

# Do all of these using one loop:

# Print every product like:

# P101 : Mouse : ₹500 : Stock 10
# Count the number of available products (stock > 0).
# Count the number of out-of-stock products (stock == 0).
# Find the most expensive product manually.
# Don't use max().

# Calculate the total inventory value.

# Formula:

# price × stock

# After the loop, print:

# Available products:
# Out of stock:
# Most expensive product:
# Highest price:
# Total inventory value:
# Rules
# ✅ One loop only
# ✅ Use items()
# ❌ No max()
# ❌ No sum()
# ❌ Don't create another loop
# Think about the variables you'll need

# You'll probably need something like:

# available = 0
# out_of_stock = 0
# highest_price = 0
# highest_product = ""
# total_value = 0

# But you decide the exact variables and logic.

# This is our last dictionary question. After you solve it, dictionary chapter = DONE, and we'll move immediately to the next Python topic.

products = {
    "P101": {
        "name": "Mouse",
        "category": "Electronics",
        "price": 500,
        "stock": 10
    },
    "P102": {
        "name": "Keyboard",
        "category": "Electronics",
        "price": 1200,
        "stock": 0
    },
    "P103": {
        "name": "Notebook",
        "category": "Stationery",
        "price": 80,
        "stock": 25
    },
    "P104": {
        "name": "Monitor",
        "category": "Electronics",
        "price": 8000,
        "stock": 5
    }
}

available_stock = 0
unavailable_stock = 0
expensive_product = 0
expensive_product_id = 0
total_value = 0
highest_price = 0

for products_id,details in products.items():
    print(products_id,details["name"],details["category"],details["price"],details["stock"],sep=" : ")
    if details["stock"] > 0:
        available_stock += 1

    if details["stock"] == 0:
        unavailable_stock += 1

    if details["price"] > highest_price:
        expensive_product = details["name"]
        highest_price = details["price"]

    total_value = details["stock"] * details["price"] + total_value
    
print("Available products:",available_stock)
print("Out of stock:",unavailable_stock)
print("Highest price:",highest_price)
print("Most expensive product:",expensive_product)
print("Total inventory value:",total_value)