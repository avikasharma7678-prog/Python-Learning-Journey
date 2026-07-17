n= int(input("Enter the number of elements in the list: "))
l = []
for i in range(n):
    element = int(input("Enter an element: "))
    l.append(element)
print(l)
l1=[]
for j in l[-1::-1]:
    l1.append(j)
print(l1)
