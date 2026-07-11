# Q11: Course Scholarship Calculator

# A learning platform has this data:

course_fee = 12000
discount_percent = 15
completed_courses = 3
student_rating = 4.6
skills = ["Python", "SQL"]
referral_code = "SAVE500"
valid_codes = ["SAVE500", "NEW100"]
extra_discount = 500
wallet_balance = 11000

# Build a program that follows these exact rules.

# 1. Calculate the normal discount
normal_discount = course_fee * discount_percent / 100

# 2. Check scholarship eligibility
# The student is eligible only when all these conditions are true:
# Completed courses are at least 2
# Student rating is at least 4.5
# "Python" is present in skills
# Store the result in:
# It should contain True or False.

scholarship_eligible = (completed_courses >= 2) and (student_rating >=4.5) and ("Python" in skills)

# 3. Approve the extra discount
# The extra discount is approved only when:
# The student is scholarship eligible AND The referral code is present in valid_codes
# Store 500 when approved; otherwise store 0.
# Variable name:
# Use a ternary expression.

approved_extra_discount = 500 if scholarship_eligible and referral_code == "SAVE500" else 0

# 4. Calculate the final course fee
final_fee = course_fee - normal_discount - approved_extra_discount

# 5. Check whether the wallet has enough money
# Wallet balance must be greater than or equal to the final fee
# Store the Boolean result in:

can_purchase = wallet_balance >= final_fee

# 6. Create the purchase status
# Store:
# "Purchase Successful" when can_purchase is True; otherwise store "Insufficient Balance"
# Use a ternary expression.

purchase_status = "Purchase Successful" if can_purchase == True else "Insufficient Balance"

# 7. Calculate the remaining wallet balance
# When the purchase is possible:
# Otherwise, the remaining balance should stay equal to the original wallet balance.

remaining_balance = wallet_balance - final_fee if can_purchase == True else wallet_balance


# Print these labeled outputs
print("Normal discount:",normal_discount)
print("Scholarship eligible:",scholarship_eligible)
print("Approved extra discount:",approved_extra_discount)
print("Final course fee:",final_fee)
print("Can purchase:",can_purchase)
print("Purchase status:",purchase_status)
print("Remaining wallet balance:",remaining_balance)