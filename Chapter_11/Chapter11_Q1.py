# Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class twoDvector:
    def var(self, x, y):
        self.x=x
        self.y=y
        print(f"These are the value of {self.x}x and {self.y}y ")

class threeDvector(twoDvector):
    def var(self,x, y, z):
        super().var(x,y)
        self.z=z
        print(f"These are the value of {self.x}x,{self.y}y and {self.z}z")

o=twoDvector()
o.var(1,2)
o2=threeDvector()
o2.var(3,4, 5)