# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways. 
from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo=trainNo

    def book(self, fro, to):
        print(f"The train is booked in train no {self.trainNo} from {fro} to {to}")

    def getStatus(self, fro, to):
        print(f"The train is going from {fro} to {to} and number of seats available are {randint(100, 500)}")

    def getFare(self, fro, to):
        print(f"The fair of the train is {randint(100, 500)} which is going from {fro} to {to}")

obj=Train(123)
obj.book("delhi", "mumbai")
obj.getStatus("delhi", "mumbai")
obj.getFare("delhi", "mumbai")