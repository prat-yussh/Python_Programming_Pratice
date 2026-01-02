# Add a static method in problem 2, to greet the user with hello. 

# Write a class “Calculator” capable of finding square, cube and square root of a number. 
import math

class Calculator:
    def __init__(self, square, cube, sqrt):
        self.square=square*square
        self.cube=cube ** 3
        self.sqrt=math.sqrt(sqrt)
    
    def __str__(self):
        return(
            f"square={self.square}\n"
            f"cube={self.cube}\n"
            f"sqrt={self.sqrt}"
        )
    
    @staticmethod
    def demo():
        print("Here is your answer.")

v=Calculator(4, 4, 4)
print(v)
v.demo()