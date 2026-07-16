def sum_of_n(n):
    if n==0:
        return 0
    x=n+sum_of_n(n-1)
    return x
x=int(input("Enter the number: "))
u=sum_of_n(x)
print(u)