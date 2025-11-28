"""
Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
"""

sub1=int(input("Enter first subject mark:"))
sub2=int(input("Enter second subject mark:"))
sub3=int(input("Enter third subject mark:"))

avg=(100*(sub1+sub2+sub3))/300

if(avg>40 and sub1>=33 and sub2>=33 and sub3>=33):
    print("The student passed the exam and the avg is:", avg)
else:
    print("The student failed the exam and the avg is:", avg)
