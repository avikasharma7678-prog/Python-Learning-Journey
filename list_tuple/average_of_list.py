n= int(input("Enter the number of elements in the list: "))
l = []
for i in range(n):
    element = int(input("Enter an element: "))
    l.append(element)
sum=0
for i in range(n):
    sum += l[i]
average = sum / n
print("The average of the elements in the list is:", average)