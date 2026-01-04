# Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

class Animals:
    def __init__(self):
        pass

class Pets(Animals):
    def __init__(self):
        super().__init__()

class Dog(Pets):
    def __init__(self):
        super().__init__()

    
    def bark(self):
        print("Woof Woof!")

obj=Dog()
obj.bark()