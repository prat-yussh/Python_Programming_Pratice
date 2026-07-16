# Q4: ATM PIN Verification

# A user gets a maximum of 3 attempts to enter the correct ATM PIN.

correct_pin = 4826

# Exact requirements
# Start the attempt count at 1.
attempt_count = 1
# Ask the user to enter the PIN.
# When the PIN is correct:
# print Login successful;
# stop asking for the PIN.
# When the PIN is wrong:
# print Incorrect PIN;
# increase the attempt count.
# After three incorrect attempts, print:
# Account locked
# The program must never ask for more than three PIN attempts.
while attempt_count<=3:
    pin = int(input("Enter the pin:"))
    if pin==correct_pin:
        print("Login successful")
        break
    else:
        print("Incorrect PIN")
    if attempt_count==3:
        print("Account locked")
        break
    attempt_count = attempt_count+1
