"""
6. Write a program to mine a log file and find out whether it contains "python". 
7. Write a program to find out the line number where python is present from ques 6. 
"""

with open("log.txt") as f:
    content=f.readlines()
    
line=1
for i in content:
    if("python" in i):
        print(f"It contains python word in line {line}")
        break
    line+=1
else:
    print("It doesnt contains python word")