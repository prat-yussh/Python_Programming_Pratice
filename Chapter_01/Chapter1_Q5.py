"""4. Write a python program to print the contents of a directory using the os module. Search online for the function which does that.
5. Label the program written in problem 4 with comments. """

# First we need to import the os module which provides a way of using operating system dependent functionality.
import os

# then we specify the directory whose contents we want to list. Here, we are using the root directory '/'.
directory='/'

# then we use the listdir() function from the os module to get a list of the contents of the specified directory.
contents=os.listdir(directory)

# Finally, we iterate through the list of contents and print each item.
for item in contents:
    print(item)