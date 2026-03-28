"""
Remove Duplicate Characters
User enters a string.

Remove duplicate characters.
Example
Input: AABBCCDDA
Output: ABCD
"""
text=input("Enter a string to remove duplicate:")
result=""
for i in text:
    if i not in result:
        result+=i
print(result)