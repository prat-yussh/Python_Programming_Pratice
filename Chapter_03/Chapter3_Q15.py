"""
Count Vowels
User enters a string.

Count how many vowels are present.
Vowels = a e i o u

Example
Input
education

Output
5
"""
mainString=input("Enter a string:").lower()

count=0

for ch in mainString:
    if ch in "aeiou":
        count+=1

print(count)