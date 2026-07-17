x=input("Enter the string: ")
s=x.find("  ")
while s != -1:
    print("double space is at:",s)
    s=x.find("  ",s+2)
