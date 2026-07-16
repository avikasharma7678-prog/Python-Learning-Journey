n=int(input("Enter the number u want to check for same first and last digits: "))
last_digit=n%10
x=n
while x>=10:
    x= x//10
if x==last_digit:
    print("Yes first and last digits are same")
else:
    print("No first and last digits are not same")
exit()