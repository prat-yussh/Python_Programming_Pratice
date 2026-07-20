# Q1: Weekly Sales Correction

# The values represent sales from Monday to Friday.

# Do exactly this:

# Print Monday’s sales using positive indexing.
# Print Friday’s sales using negative indexing.
# Print sales from Tuesday to Thursday using slicing.
# Wednesday’s correct sales were 1080. Update the list using its index.
# Print the updated complete list.
# Print the list in reverse using slicing.

# Do not use a loop or any list method yet.

daily_sales = [1200, 1450, 980, 1600, 1750]

print("Monday sales:",daily_sales[0])
print("Friday sales:",daily_sales[-1])
print("Tuesday to Thrsday sales:",daily_sales[1:-1])
daily_sales[3] = 1800
print("Updated sales:",daily_sales)
print("Updated sales:",daily_sales[::-1])