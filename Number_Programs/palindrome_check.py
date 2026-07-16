n=int(input("Enter the number to be checked for palindrome:"))
x=n
digit=0
rev=0
while x>0:
    digit=x%10
    rev=rev*10+digit
    x=x//10
if n== rev:
    print("yes,its a palindrome")
else:
    print("no,its not a palindrome")