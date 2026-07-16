x=int(input("Enter the number:"))
larg=x%10
while x>0:
    dig=x%10
    if dig>larg:
        larg=dig
    x=x//10
print("The largest digit is: ",larg)

