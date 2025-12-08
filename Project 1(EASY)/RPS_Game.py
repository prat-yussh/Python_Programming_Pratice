import random

choices={
    1:"Rock",
    2:"Paper",
    3:"Scissor"
}

computer = random.choice([1,2,3])
computer_wins=0
user_wins=0

for i in range(1,4):

    print("Choose only one!\nRock:1\nPaper:2\nScissor:3")
    user=int(input("Enter you choice:"))
    print("")

    if(computer==user):
        print("--------------\nIts a draw\n--------------")
        print("")
        print(f"Computer score={computer_wins}")
        print(f"User score={user_wins}")

    else:
        if(computer==1 and user==2):
            print("--------------\nYou Win\n--------------")
            print("")
            user_wins=user_wins+1
            print(f"Computer score={computer_wins}")
            print(f"User score={user_wins}")

        elif(computer==1 and user==3):
            print("--------------\nComputer Wins\n--------------")
            print("")
            computer_wins=computer_wins+1
            print(f"Computer score={computer_wins}")
            print(f"User score={user_wins}")

        elif(computer==2 and user==1):
            print("--------------\nComputer Wins\n--------------")
            print("")
            computer_wins=computer_wins+1
            print(f"Computer score={computer_wins}")
            print(f"User score={user_wins}")

        elif(computer==2 and user==3):
            print("--------------\nYou Wins\n--------------")
            print("")
            user_wins=user_wins+1
            print(f"Computer score={computer_wins}")
            print(f"User score={user_wins}")

        elif(computer==3 and user==1):
            print("--------------\nYou Wins\n--------------")
            print("")
            user_wins=user_wins+1
            print(f"Computer score={computer_wins}")
            print(f"User score={user_wins}")
            
        elif(computer==3 and user==2):
            print("--------------\nComputer Wins\n--------------")
            print("")
            computer_wins=computer_wins+1
            print(f"Computer score={computer_wins}")
            print(f"User score={user_wins}")

        else:
            print("--------------\nSomething Went Wrong\n--------------")
            print("")

    print(f"Computr choice:{choices[computer]}\nUSer Choice:{choices[user]}\n")

if(computer_wins>user_wins):
    print(f"Finally Computer Wins And his point is {computer_wins}")

elif(user_wins<computer_wins):
    print(f"Finally User Wins And his point is {user_wins}")

elif(user_wins==computer_wins):
    print(f"Finally Its a Draw And Both of you get same points {user_wins} {computer_wins}\n")
