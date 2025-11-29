"""
Write a program to calculate the grade of a student from his marks from the 
following scheme: 
90 = 100 => Ex 
80 = 90 => A 
70 = 80 => B 
60 = 70 =>C 
50 = 60 => D 
    <50 => F
"""

sub1=int(input("Enter your marks:"))
sub2=int(input("Enter your marks:"))
sub3=int(input("Enter your marks:"))

avg=(100*(sub1+sub2+sub3))/300

if(avg>=90 or avg<=100):
    print("His grade is:Ex")
elif(avg>=80 or avg<=90):
    print("His grade is:A")
elif(avg>=70 or avg<=80):
    print("His grade is:B")
elif(avg>=60 or avg<=70):
    print("His grade is:C")
elif(avg>=50 or avg<=60):
    print("His grade is:D")
elif(avg<50):
    print("His grade is:F")
