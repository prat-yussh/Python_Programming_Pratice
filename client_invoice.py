# Q8: Department Sales Matrix

# Each inner list represents one department:

# Index 0 → Electronics
# Index 1 → Clothing
# Index 2 → Grocery

# Each value represents sales for Monday, Tuesday, and Wednesday.

# Do exactly this:

# Print Clothing’s Tuesday sales using nested indexing.
# Change Grocery’s Monday sales from 2000 to 2100.
# Print the complete Grocery sales list.
# Use nested for loops to print the matrix like this:
# 1200 1500 1800
# 900 1100 1300
# 2100 2200 2500

# Do not use sum() or any list method. Nested lists represent table-like or matrix data.

sales = [
    [1200, 1500, 1800],
    [900, 1100, 1300],
    [2000, 2200, 2500]
]

print("Clothing tuesday:",sales[1][1])
sales[2][0] = 2100 
print("Grocery:",sales[2])
for row in sales:
    for amount in row:
        print(amount, end=" ")
    print()