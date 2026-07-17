n= int(input("Enter the number of elements in the list: "))
l = []
for i in range(n):
    element = int(input("Enter an element: "))
    l.append(element)
l1 = []
for i in l:
    if i not in l1:
        l1.append(i)
print("The list after removing duplicates is:", l1)