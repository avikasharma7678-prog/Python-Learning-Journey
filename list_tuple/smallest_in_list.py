n= int(input("Enter the number of elements in the list: "))
l = []
for i in range(n):
    element = int(input("Enter an element: "))
    l.append(element)
smallest = l[0]
for i in range(n):
    if l[i] < smallest:
        smallest = l[i]
print("The smallest element in the list is:", smallest)