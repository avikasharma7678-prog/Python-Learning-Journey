x=int(input("Enter the number:"))
small=x%10
while x>0:
    dig=x%10
    if dig<small:
        small=dig
    x=x//10
print("The smallest number is: ",small)