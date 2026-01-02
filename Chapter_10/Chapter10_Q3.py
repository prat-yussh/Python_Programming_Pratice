#  Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute? 

class demo:
    a=5

obj=demo() #obj allocation
obj.a=0 #set value
print(obj.a) #print new seted value
print(demo.a) #but here the class attribute is not changed