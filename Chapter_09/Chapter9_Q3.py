# Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old. 

for i in range(2,21):
    with open(f"Chapter_09/Tables/Tables_{i}.txt", "w") as f:
        f.write(f"This is multiplication table of {i}\n")
        for j in range(1,11):
            f.write(f"{i} X {j} = {i*j}\n")

# import os

# # Create a folder named "Tables" if it doesn't exist
# os.makedirs("Tables", exist_ok=True)

# # Generate tables from 2 to 20
# for i in range(2, 21):
#     with open(f"Tables/Table_{i}.txt", "w") as file:
#         file.write(f"Multiplication Table of {i}\n")
#         file.write("-" * 30 + "\n")

#         for j in range(1, 11):
#             file.write(f"{i} x {j} = {i * j}\n")

#         file.write("\nBest of luck, champ! 😊\n")
