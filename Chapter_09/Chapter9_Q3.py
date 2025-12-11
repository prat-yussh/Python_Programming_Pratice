# Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old. 
with open("Multi_Plication_Table.txt", "w+") as f:
    for i in range(2,21):
        print("Best Of Luck Buddy😊")
        print("")
        print(f"This is Multiplication Table of:{i}")
        for j in range(1,11):
            print(f"{i} X {j} = {i*j}")