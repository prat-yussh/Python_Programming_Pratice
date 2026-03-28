"""
Reverse Words Order

User enters a sentence.
Reverse word order.

Example
Input: I love python
Output: python love I
"""
text=input("Enter a string:")
words=text.split()
words.reverse()
print(" ".join(words))