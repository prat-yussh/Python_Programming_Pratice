# Write a python program to rename a file to “renamed_by_ python.txt.

import os

old_name = "example.txt"

new_name = "renamed_by_python.txt"

os.rename(old_name, new_name)

print("File renamed successfully!")
