# Set Data Structure: Q1

# A website records visitor IDs, but some visitors appear more than once:

# Do exactly this:

# Convert visitor_ids into a set named unique_visitors.
# Print the original number of entries.
# Print the number of unique visitors.
# Print unique_visitors.
# Check whether "V104" exists in the set.
# Print either:
# V104 visited

# or:

# V104 did not visit

# Use only:

# set()
# len()
# in

# Do not use a loop.

# A set removes duplicate values automatically and does not support indexing. The displayed order may differ because sets do not preserve positional order.

visitor_ids = ["V101", "V102", "V101", "V103", "V102"]
unique_visitors = set(visitor_ids)

print("original number",visitor_ids)
print("number of unique visitors",len(unique_visitors))
print("number of unique visitors",unique_visitors)

if "V104" in unique_visitors:
    print("V104 visited")
else:
    print("V104 did not visit")