"""
Login System (Core Programming Logic)

User has:

username = "admin"
password = "1234"

User gets 3 attempts.

If correct → print "Login Successful"
If all attempts fail → "Account Locked"

Think:
What loop?
What variable tracks attempts?
When should loop stop?

Explain thinking.
"""

username = "admin"
password = "1234"

attempt=1

while attempt<=3:
    usernameInput=input("Enter your username:")
    passwordInput=input("Enter your password:")
    if username == usernameInput and password == passwordInput:
        print("Login Successful")
        break
    attempt=attempt+1
else:
    print("Account Locked")

"""
step-1:First we set "username" and "password"
step-2:set "attempt=1"
step-3:Then we use while loop and check "attempt<=3"
step-4:Then we Input from user and store it inside "usernameInput" and "passwordInput"
step-5:INcrement "attempt value to + 1"
step-6:Then if "username == usernameInput and password == passwordInput"
        Login Successful
step-7:else 
        Account Locked
"""