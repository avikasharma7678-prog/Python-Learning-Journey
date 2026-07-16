n=int(input("Enter the number of digits:"))
s=0
x=1
if n==1:
    print(s,end="")
elif n==0:
    print("0")
else:
    print(s,end="")
    print(x,end="")
for i in range(n-2):
    y=x+s
    print(y,end="")
    s=x
    x=y
    

    