"""
A spam comment is defined as a text containing following keywords: 
""Make a lot of money”, ""buy now”, ""subscribe this”, ""click this”. 
Write a program to detect these spams.
"""
w1="Make a lot of money"
w2="buy now"
w3="subscribe this" 
w4="click this"

comment=input("Enter your comment:")

if(w1 in comment or w2 in comment or w3 in comment or w4 in comment):
    print("its a spam comment")
else:
    print("its not a spam comment")
