# Q8: Final Flow-Control Challenge

# A parking lot has space for 5 vehicles.

# Repeatedly ask the user to enter a vehicle number.
# Exact rules
# Start:
# When the user enters "close":
# stop accepting vehicles;
# print the final report.
# When the user enters an empty value:
# print Invalid vehicle number;
# skip it.
# When five vehicles have already been parked:
# print Parking full;
# increase rejected_vehicles by 1;
# stop the program.
# Otherwise:
# print Vehicle parked;
# increase parked_vehicles by 1.
# After the loop, print:
# Parked vehicles:
# Rejected vehicles:
# Available spaces:

# Formula:

# Available spaces = 5 − Parked vehicles

parked_vehicles = 0
rejected_vehicles = 0

while True:
    vehicle_number = input("enter a vehicle number:")
    
    if vehicle_number == "close":
        break
    elif vehicle_number == "":
        print("Invalid vehicle number")
        continue
    elif parked_vehicles == 5:
        print("Parking full")
        rejected_vehicles += 1
        break
    else:
        print("Vehicle parked")
        parked_vehicles += 1

available_space = 5 - parked_vehicles
print("Parked vehicle:",parked_vehicles)
print("Rejected vehicle:",rejected_vehicles)
print("Available space:",avilable_space)