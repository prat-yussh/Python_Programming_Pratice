# Q2: Trip Expense Splitter

# Three friends went on a trip. The user will enter these three expenses in one line, separated by commas:

# Fuel,Food,Toll

# Example input:

# 1500,900,300

# The user will then enter the number of travellers:

# 3
# Program requirements
# Read fuel, food, and toll expenses using one input statement.
# Convert all three expenses to float.
# Read the number of travellers and convert it to int.
# Calculate:
# Total expense = Fuel + Food + Toll
# Cost per traveller = Total expense ÷ Number of travellers
fuel,food,toll = [float(value) for value in input("fuel,food,toll:").split(",")]
number_of_traveller = int(input("number of travellers:"))
total_expenses = fuel + food + toll
cost_per_travell = total_expenses / number_of_traveller

print("------ TRIP EXPENSE ------")
print("Fuel:",fuel)
print("Food:",food)
print("Toll:",toll)
print("Total expense:",total_expenses)
print("Travellers:",number_of_traveller)
print("Cost per traveller:",cost_per_travell)
print("---------------------")