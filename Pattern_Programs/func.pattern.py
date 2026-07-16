def pattern(n):
    for i in range(1,n+1):
        print("*"*(n-i+1))
x= int(input("Enter the number:"))
pattern(x)