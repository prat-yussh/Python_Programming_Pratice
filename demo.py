# PDF 2 — Q10: Freelance Payment Calculator

# A freelancer completed a project.

hours_worked = 18
hourly_rate = 700
platform_fee_percent = 8
client_rating = 4.7
delivered_on_time = True
skills = ["Python", "SQL", "Git"]
bonus = 1500

# Build a program that does exactly this
# Calculate the freelancer’s gross earning.
gross_earning = hours_worked * hourly_rate
print("Grioss earning:",gross_earning)

# Calculate the platform fee amount.
platform_fee = gross_earning * 8 / 100
print("Platform fee:",platform_fee)

# Check whether the freelancer knows both Python and SQL.
req_skills = "YES" if "Python" in skills and "SQL" in skills else "NO"
print("Has required skills:",req_skills)

# Approve the bonus only when all three rules are true:
# Client rating is at least 4.5 AND Project was delivered on time AND Both Python and SQL are present in skills
approved_bonus = "YES" if client_rating >= 4.5 and delivered_on_time and "Python" in skills and "SQL" in skills else "NO"
print("Bonus approved:",approved_bonus)

# Store either 1500 or 0 as the approved bonus amount using a ternary operator.
bonus_amount = bonus if approved_bonus == "YES" else 0
print("Approved bonus amount:",bonus_amount)

# Calculate the final earning:
final_earning = gross_earning - platform_fee +bonus_amount
print("Final earning:",final_earning)

# Store this message using a ternary operator: "Bonus Approved" or "Bonus Not Approved"
status = "Bonus Approved" if bonus_amount == 1500 else "Bonus Not Approved"  
print("Status:",status)