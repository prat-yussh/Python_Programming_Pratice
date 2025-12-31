# Write a program to find out whether a file is identical & matches the content of another file.

with open("Chapter_09/Hi-score.txt") as f:
    content1=f.read()
    
with open("Chapter_09/Chapter9_Q8.txt") as f:
    content2=f.read()

if(content1 == content2):
    print("Yes this files are identical")
else:
    print("No this files are not identical")