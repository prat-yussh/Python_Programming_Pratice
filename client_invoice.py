# Q8: Calculate Tuple Total and Average

# Do exactly this:

# Create total_sales = 0.
# Use a for loop to add every value manually.
# Calculate:
# Average = total sales / number of values
# Print:
# Total sales: 5600
# Average sales: 1400.0

# Rules:

# Do not use sum().
# Use len() when calculating the average.
# Do not convert the tuple into a list.

# This is the practical tuple program included near the end of the chapter.

monthly_sales = (1200, 1500, 1100, 1800)
total_sales = 0

for sale in monthly_sales:
    total_sales += sale

average_sales = total_sales / len(monthly_sales)

print("Total sales:", total_sales)
print("Average sales:", average_sales)