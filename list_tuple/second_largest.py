n= int(input("Enter the number of elements in the list: "))
l = []
for i in range(n):
    element = int(input("Enter an element: "))
    l.append(element)
largest=l[0]
second_largest=0
for i in range(n):
    if l[i]>largest:
        second_largest=largest
        largest=l[i]
    else:
        continue
print("The second largest element in the list is:", second_largest)