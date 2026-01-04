"""
Create a class ‘Employee’ and add salary and increment properties to it. 

Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter 

which changes the value of increment based on the salary.
"""

class Employee:
    def __init__(self, name, salery, saleryIncrement):
        self.name=name
        self.salery=salery
        self.saleryIncrement=self.salery+500

o=Employee("Pratyush",500)

