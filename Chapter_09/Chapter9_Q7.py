"""
6. Write a program to mine a log file and find out whether it contains "python". 
7. Write a program to find out the line number where python is present from ques 6. 
"""

with open("log.txt", "r") as f:
    content=f.read()
    if("python" in content):
        print("It contains python word")
    else:
        print("It doesnt contains python word")