def add(a,b):
    ans=a+b
    print(ans)
    lst.append(ans)
def sub(a,b):
    ans=b-a
    print(ans)
    lst.append(ans)
def mul(a,b):
    ans=a*b
    print(ans)
    lst.append(ans)
def div(a,b):
    if a=='0':
        print("NOT APPLICABLE")
    else:
        ans=b/a
        print(ans)
        lst.append(ans)
lst=[]
while 1 :
    print("PYTHON CALCULATOR")
    ch=input("1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.EXIT\n6.HISTORY\nEnter your choice: ")
    if ch == '1':
        num1=int(input("Enter first number: "))
        num2=int(input("Enter second number: "))
        add(num1,num2)
    elif ch == '2':
        num1=int(input("Enter first number: "))
        num2=int(input("Enter second number: "))
        sub(num1,num2)
    elif ch == '3':
        num1=int(input("Enter first number: "))
        num2=int(input("Enter second number: "))
        mul(num1,num2)
    elif ch == '4':
        num1= int(input("Enter divisor: "))
        num2= int(input("Enter dividend: "))
        div(num1,num2)
    elif ch == '5':
        exit()
    elif ch == '6':
        print(lst)
    else: 
        print("Enter Valid Choice!")