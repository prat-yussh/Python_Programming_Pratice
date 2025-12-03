#  Write a python function which converts inches to cms.

def converter(inch):
    value=inch*2.54
    print(f"the cms is:{value}")


inch=int(input("Enter a number to onverts inches to cms:"))
converter(inch)