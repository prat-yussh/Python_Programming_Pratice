"""
What is dangerous about this?
x = eval(input("Enter something: "))

Why should we avoid eval() in real projects?
"""
x = eval(input("Enter something: ")) #eval() is dangerous because it executes arbitrary user input as real Python code, which can lead to serious security vulnerabilities.