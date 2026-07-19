# Q3: Error Log Keyword Tracker

# Ask the user to enter:

# a log message;
# a keyword to search.

# Example:

# Log: error timeout error network error
# Keyword: error

# Print every starting index of the keyword:

# Found at position: 0
# Found at position: 14
# Found at position: 28
# Total occurrences: 3
# Exact requirements
# Apply .strip().lower() to both inputs.
# Use find() inside a while loop.
# After finding a match, continue searching from the next position.
# Count the occurrences manually.
# When no match exists, print:
# Keyword not found
# Do not use count().

log = input("Enter a log message:").strip().lower()
keyword = input("Enter a keyword to search:")
occurences = 0
start_postion = 0 

while True:
    postion = log.find(keyword,start_postion)
    
    if postion == -1:
        break
    
    print("Found at postion:",postion)
    occurences += 1
    start_postion = postion + 1

if occurences == 0:
    print("Not found")

else:
    print("occurences:",occurences)