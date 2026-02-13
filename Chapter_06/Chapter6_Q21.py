"""
User enters age.

Print:

"Child" (0–12)
"Teen" (13–19)
"Adult" (20–59)
"Senior" (60+)

How will you structure this cleanly?
"""

age=int(input("Enter your age:"))

if age>=0 and age<=12:
    print("Child")

elif age>=13 and age<=19:
    print("Teen")

elif age>=20 and age<=59:
    print("Adult")

else:
    print("Senior")
