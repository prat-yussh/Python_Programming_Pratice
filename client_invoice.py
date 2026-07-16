# Q5: Online Order Processing

# The user enters six product prices in one line, separated by spaces.

# Example:

# Enter 6 prices: 500 1200 -50 800 6000 300
prices = [int(value) for value in input("Enter 6 prices:").split()]
# Process each price from left to right.

# Exact rules
# Start:
total_amount = 0
processed_items = 0
# When a price is 0 or negative:
# print Invalid price skipped: <price>
# skip that price;
# continue processing the next price.
# When a price is greater than 5000:
# print Manual approval required: <price>
# stop processing immediately.
# Prices after it must not be processed.
# For every valid price from 1 to 5000:
# add it to total_amount;
# increase processed_items by 1;
# print Item processed: <price>.
# After processing, print:
# Processed items:
# Total amount:
# When all six prices are processed without stopping because of a price above 5000, also print:
# All items processed successfully
for price in prices:
    if price <= 0:
        print("Invalid price skipped:",price)
        continue
    elif price > 5000:
        print("Manual approval required:",price)
        break
    else:
            total_amount += price
            processed_items += 1
            print("Item processed:", price)

else:
    print("All items processed successfully")


# Use for, continue, break, and the loop’s else block. Do not use sum() or count().