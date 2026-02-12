"""
cart = [10, 20, 600, 30]
for item in cart:
    if item > 500:
        print("Stop")
        break
    print(item)
else:
    print("All processed")

    
Will "All processed" print?
"""

cart = [10, 20, 600, 30]
for item in cart:
    if item > 500:
        print("Stop")
        break
    print(item)
else:
    print("All processed")
# "All processed" will not print because once loop hit item > 500 it come out of the loop
# output
# 10 
# 20
# Stop