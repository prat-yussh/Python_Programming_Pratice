# Q3: Tuple Search

# Do exactly this:

# Print how many times "IT" appears using count().
# Print the index of the first "Finance" using index().
# Check whether "Marketing" exists in the tuple.
# Print either:
# Marketing available

# or:

# Marketing not available

# Do not use a loop.

departments = ("Sales", "HR", "IT", "Finance", "IT")

print("IT count:", departments.count("IT"))
print("Finance index:", departments.index("Finance"))

if "Marketing" in departments:
    print("Marketing available")
else:
    print("Marketing not available")