import random

choices={
    1:"Rock",
    2:"Paper",
    3:"Scesor"
}

random_number = random.choice([1,2,3])
# computr = choices[random_number]

print("Choose only one!\nRock:1\nPaper:2\nScissor:3")

user=int(input("Enter you choice:"))
user=choices[user]
if(computr==user):
    print("Its a draw")
else:
    if(computr==1 and user==2):
        print("You Win")
    elif(computr==1 and user==3):
        print("Computer Wins")
    elif(computr==2 and user==1):
        print("You Wins")
    elif(computr==2 and user==3):
        print("You Wins")
    elif(computr==3 and user==1):
        print("You Wins")
    elif(computr==3 and user==2):
        print("Computer Wins")
    else:
        print("Something Went Wrong")

print(f"Computr choice:{computr}\nUSer Choice:{user}")

    