n= int(input("Enter the number of elements in the list: "))
l = []
for i in range(n):
    element = int(input("Enter an element: "))
    l.append(element)
largest = l[0]
for i in range(n):
    if l[i] > largest:
        largest = l[i]
print("The largest element in the list is:", largest)