#  Write a program to make a copy of a text file “this. txt” 

with open("Chapter_09/Hi-score.txt") as f:
    content=f.read()
    
with open("Chapter_09/Chapter9_Q8.txt", "w") as f:
    f.write(content)
