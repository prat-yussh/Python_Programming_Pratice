# Q6: Command-Line Client Invoice

# Create a file named:

# client_invoice.py

# Run it like this:

# python client_invoice.py "Rahul Kumar" 6 850 500

# The arguments represent:

# "Rahul Kumar" → client name
# 6             → videos edited
# 850           → price per video
# 500           → bonus

# The quotation marks keep Rahul Kumar together as one command-line argument. Command-line arguments arrive as strings, so numeric values must be converted before calculation.

# Exact requirements
# Read all four values from command-line arguments.
# Convert:
# videos to int
# price per video to float
# bonus to float
# Calculate:
# Editing charge = Videos × Price per video
# Final payment = Editing charge + Bonus
# Print this report:
# ------ CLIENT INVOICE ------
# Client: Rahul Kumar
# Videos: 6 | Price per video: 850.0
# Editing charge: 5100.0
# Bonus: 500.0
# Final payment: 5600.0
# ----------------------------
# Use .format() to create this particular line:
# Videos: 6 | Price per video: 850.0
from sys import argv

name = (argv[1])
videos_edited = int(argv[2])
price_per_video = float(argv[3])
bonus = float(argv[4])

editing_charge = videos_edited * price_per_video
final_payment = editing_charge + bonus

print("------ CLIENT INVOICE ------")
print("Client:",name)
print("Videos:{} | Price per video:{}".format(videos_edited,price_per_video))
print("Editing charge:",editing_charge)
print("Bonus:",bonus)
print("Final payment:",final_payment)
print("----------------------------")