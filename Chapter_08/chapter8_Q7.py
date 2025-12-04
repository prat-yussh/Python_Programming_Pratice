#  Write a python function to remove a given word from a list ad strip it at the same time.

def move(l,word):
    n=[]
    for i in l:
        if not(i == word):
            n.append(i.strip(word))
    return n


l=["harry","pratyush","omm","chinmay"]
word=input("Enter a word to remove from the list:")

print(move(l,"word"))