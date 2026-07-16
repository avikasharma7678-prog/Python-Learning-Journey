x=int(input("Enter the number:"))
sum=0
while x>0:
    dig=x%10
    sum += dig
    x=x//10
print(sum)