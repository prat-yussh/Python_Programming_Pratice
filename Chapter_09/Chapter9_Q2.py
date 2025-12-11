#  The game() function in a program lets a user play a game and returns the score as an integer. You need to write a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score. 

def game():
    import random

    choices={
        1:"Rock",
        2:"Paper",
        3:"Scissor"
    }

    computer_wins=0
    user_wins=0

    for i in range(1,6):
        computer = random.choice([1,2,3])

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
        with open("Hi-score.txt" , "a+") as f:
            w=f.write(f"\nLast time Computer Winns and his score is:{computer_wins}\n")
            # print(f"Last time Computer Winns and his score is:{computer_wins}\n")

    elif(user_wins>computer_wins):
        print(f"Finally User Wins And his point is {user_wins}")
        with open("Hi-score.txt" , "a+") as f:
            w=f.write(f"\nLast time User Wins and his score is:{user_wins}\n")
            # print(f"Last time User Wins and his score is:{user_wins}\n")


    elif(user_wins==computer_wins):
        print(f"Finally Its a Draw And Both of you get same points {user_wins} {computer_wins}\n")

        with open("Hi-score.txt" , "a+") as f:
            w=f.write(f"\nLast time Both of you got same points\nComputer point:{computer_wins}\nUser point:{user_wins}\n")
            # print(f"Last time Both of you got same points\nComputer point:{computer_wins}\nUser point:{user_wins}")

game()