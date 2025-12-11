# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’. 

with open("poems.txt") as f:
    w=f.read()
    if ("twinkle" in w):
        print("It contains Twinkle")
    else:
        print("It doesnt contains Twinkle")