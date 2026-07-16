x=int(input("Enter the number u want to reverse"))
rev=0
digit=0
while x != 0:
    digit=x%10
    rev=rev*10+digit
    x=x//10
print(rev)