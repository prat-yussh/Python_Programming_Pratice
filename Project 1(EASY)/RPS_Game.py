import random

choices={
    1:"Rock",
    2:"Paper",
    3:"Scissor"
}

computer = random.choice([1,2,3])

for i in range(1,4):

    print("Choose only one!\nRock:1\nPaper:2\nScissor:3")
    user=int(input("Enter you choice:"))
    print("")


    if(computer==user):
        print("Its a draw")
        print("")
    else:
        if(computer==1 and user==2):
            print("You Win")
            print("")
        elif(computer==1 and user==3):
            print("Computer Wins")
            print("")
        elif(computer==2 and user==1):
            print("Computer Wins")
            print("")
        elif(computer==2 and user==3):
            print("You Wins")
            print("")
        elif(computer==3 and user==1):
            print("You Wins")
            print("")
        elif(computer==3 and user==2):
            print("Computer Wins")
            print("")
        else:
            print("Something Went Wrong")
            print("")

    print(f"Computr choice:{choices[computer]}\nUSer Choice:{choices[user]}\n")    