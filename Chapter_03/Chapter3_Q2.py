"""
Write a program to fill in a letter template given below with name and date.
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
"""

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

name=input("Enter your name:")
date=input("Enter date:")

name_output=letter.replace("<|Name|>",name)
# var=name_output
date_output=name_output.replace("<|Date|>",date)
 

print(date_output)