# A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file. 

with open("Chapter9_Q4(Donkey).txt", "r") as f:
    content=f.read().strip().lower()
    updated_content=content.replace("donkey","#####")
    with open("Chapter9_Q4(Donkey).txt", "w") as f:
        f.write(updated_content)