# Final Challenge: Client Payment Receipt

# Ask the user to enter:

client_name = input("Enter your name:")
# Three values in one line separated by commas:
# Number of videos, price per video, bonus

# Example input:

# Client name: Rahul
number_of_videos, price_per_videos, bonus = input("Enter videos,price and bonus:").split(",")

number_of_videos, price_per_videos, bonus = (
    int(number_of_videos),
    float(price_per_videos),
    float(bonus)
    )
# Exact requirements
# Convert number of videos to int.
# Convert price and bonus to float.
# Calculate:
editing_charge = number_of_videos * price_per_videos
final_payment = editing_charge + bonus
# Print the client name, videos, and price on one line separated by |.

# Show all money values with exactly two decimal places.
# Use two separate print() statements with end to display:

# Receipt generated successfully
# Required output format
print("------ PAYMENT RECEIPT ------")
print(client_name,number_of_videos,price_per_videos,sep=" | ")
print("Editing charge: ₹{:.2f}".format(editing_charge))
print("Bonus: ₹{:.2f}".format(bonus))
print("Final payment: ₹{:.2f}".format(final_payment))
print("-----------------------------")
print("Receipt generated",end=" ")
print("successfully")