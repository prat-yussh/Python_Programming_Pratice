# Q7: Backup List and Aliasing

# Do exactly this:

# Create alias_prices using:
# alias_prices = original_prices
# Change the first value of alias_prices to 150.
# Print both lists.
# Create an independent copy named backup_prices using copy().
# Change the second value of backup_prices to 275.
# Print original_prices and backup_prices.

# Observe which change affects both lists and which does not. This practises list aliasing and cloning.

original_prices = [120, 250, 300]

alias_prices = original_prices
alias_prices[0] = 150

print("Original:", original_prices)
print("Alias:", alias_prices)

backup_prices = original_prices.copy()
backup_prices[1] = 275

print("Original:", original_prices)
print("Backup:", backup_prices)