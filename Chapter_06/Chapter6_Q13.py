"""
for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("Done")
Will "Done" print?

Why?
"""

for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("Done")
"""
Output:-
Only "0" will print becuse when the brake statement occurs at i==1 it will stop immidiatily so the else block will not run.
"""