"""
Number Guessing Game (Logic Builder ⭐)

Computer secretly chooses number = 7.
User keeps guessing until correct.

Program should tell:
"Too High"
"Too Low"
"Correct"

Think:
Which loop type?
When does loop stop?
Explain logic only.
"""

from random import randint

randomNum=randint(1,10)

while True:
    user=int(input("Enter a number:"))
    if user==randomNum:
        print("Correct")
        break
    elif user<randomNum:
        print("Too Low")
    elif user>randomNum:
        print("Too High")

"""
Start game
↓
Computer chooses secret number
↓
Repeat forever:
    Ask user for guess
    Compare guess with secret number
    If correct → stop game
    If smaller → say Too Low
    If larger → say Too High
"""