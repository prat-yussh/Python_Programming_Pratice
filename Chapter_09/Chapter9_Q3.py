# Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old. 
import os


    
for i in range(2,21):
    with open(f"{i}.txt", "a") as f:
        create=f.write()
        print(f"This is Multiplication Table of:{i}")
    for j in range(1,11):
        print(f"{i} X {j} = {i*j}")
        # print("Best Of Luck Champ 😊")