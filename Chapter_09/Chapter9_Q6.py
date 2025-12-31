#  Write a program to mine a log file and find out whether it contains ‘python’. 

with open("log.txt", "r") as f:
    content=f.read()
    # for i in content
    if("python" in content):
        print("It contains python word")
    else:
        print("It doesnt contains python word")