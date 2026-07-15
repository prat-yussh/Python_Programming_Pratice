# Q2: Personal Loan Application

# Ask the user to enter:

age = int(input("Enter age:"))
monthly_income = float(input("Enter monthly income:"))
credit_score = float(input("Enter credit score:"))
Existing_loan_status: str(input("Enter existing loan status yes or no:"))

# Apply these rules in the exact order below:

# Age below 21 or above 60:
# Application rejected: age not eligible
# Monthly income below 25000:
# Application rejected: income too low
# Credit score below 650:
# Application rejected: low credit score
# Existing loan is "yes" and monthly income is below 50000:
# Application sent for manual review
# Otherwise:
# Loan application approved

if age<21 or age>60:
    print("Application rejected: age not eligible")
elif monthly_income < 25000:
    print("Application rejected: income too low")
elif credit_score < 650:
    print("Application rejected: low credit score")
elif Existing_loan_status == "yes" and monthly_income < 50000:
    print("Application sent for manual review")
else:
    print("Loan application approved")