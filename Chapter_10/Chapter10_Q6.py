#  Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects.

from random import randint

class Train:

    def __init__(slf, trainNo): #there is no problem 
        slf.trainNo=trainNo

    def book(harry, fro, to):
        print(f"The train is booked in train no {harry.trainNo} from {fro} to {to}") #there is no problem 

    def getStatus(self, fro, to):
        print(f"The train is going from {fro} to {to} and number of seats available are {randint(100, 500)}")

    def getFare(self, fro, to):
        print(f"The fair of the train is {randint(100, 500)} which is going from {fro} to {to}")

obj=Train(123)
obj.book("delhi", "mumbai")
obj.getStatus("delhi", "mumbai")
obj.getFare("delhi", "mumbai")