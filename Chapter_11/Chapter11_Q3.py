"""
Create a class ‘Employee’ and add salary and increment properties to it. 

Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter 

which changes the value of increment based on the salary.
"""

class Employee:
    def __init__(self, name, salery):
        self.name=name
        self.salery=salery
        self.increment=0

    @property
    def salaryAfterIncrement(self):
        return self.salery+self.increment
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salery):
        self.increment=new_salery-self.salery

obj=Employee("Pratyush",45000)
obj.salaryAfterIncrement=50000
print(obj.increment)
print(obj.salaryAfterIncrement)