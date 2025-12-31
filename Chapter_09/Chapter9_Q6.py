#  Write a program to mine a log file and find out whether it contains ‘python’. 

with open("Chapter_09/log.txt", "r") as f:
    content=f.read()
    if("python" in content):
        print("It contains python word")
    else:
        print("It doesnt contains python word")