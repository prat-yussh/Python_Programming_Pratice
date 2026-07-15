# Q1: ATM Withdrawal Validator

# Create a program that asks the user for:

current_balance = int(input("Enter you current balance:"))
withdrawal_amount = int(input("Enter your eithdrawl amount:"))
# Apply the rules in this exact order
# When the withdrawal amount is 0 or negative, print:
# Invalid withdrawal amount
# Otherwise, when the amount is not a multiple of 100, print:
# Enter amount in multiples of 100
# Otherwise, when the amount is greater than the current balance, print:
# Insufficient balance
# Otherwise, when withdrawing the amount would leave less than ₹500, print:
# Minimum balance of ₹500 must be maintained
# Otherwise:
# subtract the amount from the balance;
# print Withdrawal successful;
# print the remaining balance.
# Example
# Current balance: 5000
# Withdrawal amount: 4200

after_withdrawl = current_balance - withdrawal_amount

if withdrawal_amount == 0 or withdrawal_amount<0:
    print("Invalid withdrawal amount")
elif withdrawal_amount%100 != 0:
    print("Enter amount in multiples of 100:",withdrawal_amount)
elif withdrawal_amount>current_balance:
    print("Insufficient balance")
elif after_withdrawl<500:
    print("Minimum balance of ₹500 must be maintained")
else:
    print("Withdrawal successful")
    print("Remaing balance",after_withdrawl)
    current_balance = after_withdrawl
    print("Withdrawal successful")
    print("Remaining balance:", current_balance)


# Output:

# Withdrawal successful
# Remaining balance: 800

# Use if, elif, and else. Check only one rule at a time in the order given.