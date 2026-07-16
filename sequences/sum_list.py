n= int(input("Enter the number of elements u want to add in  list: "))
lst=[]
for i in range(n):
    x=int(input("Enter the value:"))
    lst.append(x)
print(lst)
sum=0
for i in lst:
    sum=sum+i
print("The sum is:",sum)
