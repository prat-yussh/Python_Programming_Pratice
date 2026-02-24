"""
🧩 Problem 1 — ATM Withdrawal Logic

User enters:
account balance
withdrawal amount

Rules:
Amount must be multiple of 100
Amount ≤ balance
Minimum balance after withdrawal must be 500

Print:
"Transaction Successful"
or exact reason why rejected

👉 Think:
What condition should be checked first and why?

(No code first — explain logic order.)
"""

amount=int(input("Enter the amount you want to withdraw:"))

balance=30000

if amount%100==0:
    if amount<=balance:
        remaining_balance=balance-amount
        if remaining_balance<500:
            print(f"Transaction Unsuccessful\nMinimum balance after withdrawal must be 500\nAnd your balance is:{balance}")
        else:
            print(f"Transaction Successful\nAnd your balance is:{balance}")

    else:
        print(f"Balnce is low:{balance}")
else:
    print("amount must be multiple of 100\nEnter Amount\n100\n500")


"""
Step-1: Take withdrawal amount as input.

Step-2: Check whether the amount is a multiple of 100.
        If not, reject transaction.

Step-3: Check whether withdrawal amount is less than or equal to balance.
        If not, reject transaction.

Step-4: Check whether remaining balance after withdrawal is at least 500.
        If not, reject transaction.

Step-5: If all conditions pass, complete transaction successfully.
"""