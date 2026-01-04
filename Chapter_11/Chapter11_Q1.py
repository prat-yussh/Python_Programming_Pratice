# Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class twoDvector:

    def __init__(self, i, j):
        self.i=i
        self.j=j

    def var(self):
        print(f"These are the value of {self.i}i and {self.j}j ")

class threeDvector(twoDvector):

    def __init__(self, i, j, k):
        super().__init__(i,j)
        self.k=k

    def var(self):
        print(f"These are the value of {self.i}i , {self.j}j and {self.k}k")

o=twoDvector(1, 2)
o.var()
o2=threeDvector(1, 2, 3)
o2.var()
