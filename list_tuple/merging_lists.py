n1= int(input("Enter the number of elements in the first list: "))
l1=[]
for i in range(n1):
    element = int(input("Enter an element for the first list: "))
    l1.append(element)
n2= int(input("Enter the number of elements in the second list: "))
l2=[]
for i in range(n2):
    element = int(input("Enter an element for the second list: "))
    l2.append(element)
print("The first list is:", l1)
print("The second list is:", l2)
l3=l1+l2
for i in l3:
    if l3.count(i)>1:
        l3.remove(i)
print("The merged list is:", l3)
