class Programmer:
    def __init__(self, name, age, salary, office):
        self.name = name
        self.age = age
        self.salary = salary
        self.office = office

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Salary: {self.salary}\n"
            f"Office: {self.office}\n"
        )


pratyush = Programmer("Pratyush", 21, 50000000, "Microsoft")
chinmay = Programmer("Chinmay", 20, 40000000, "Microsoft")
shibham = Programmer("Shibham", 23, 30000000, "Microsoft")
rohan = Programmer("Rohan", 26, 40000000, "Microsoft")
sambid = Programmer("Sambid", 26, 30000000, "Microsoft")
karan = Programmer("Karan", 26, 20000000, "Microsoft")
minhaz = Programmer("Minhaz", 26, 70000000, "Microsoft")

print(pratyush)
print(chinmay)
print(shibham)
print(rohan)
print(karan)
print(sambid)
print(minhaz)
