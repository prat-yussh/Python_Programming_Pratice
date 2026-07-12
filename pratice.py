# Q1: Freelance Invoice Generator

# Create a program that takes all details from the user instead of using fixed values.

# User must enter
# Client name
# Number of videos edited
# Price per video
# Bonus amount
# Program must calculate
# Editing charge = Number of videos × Price per video

# Final payment = Editing charge + Bonus
# Program must print this invoice
# ------ INVOICE ------
# Client: Rahul
# Videos edited: 6
# Price per video: 850.0
# Editing charge: 5100.0
# Bonus: 500.0
# Final payment: 5600.0
# ---------------------
# Requirements
client_name = str(input("Client:"))
number_of_videos = int(input("Videos edited:"))
price_per_video = float(input("Price per video:"))
editing_charges = number_of_videos * price_per_video
print("Editing charge:",editing_charges)
bonus_amount = float(input("Bonus:"))
final_payment = editing_charges + bonus_amount
print("Final payment:",final_payment)