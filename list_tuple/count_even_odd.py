n= int(input("Enter the number of elements in the list: "))
l = []
for i in range(n):
    element = int(input("Enter an element: "))
    l.append(element)
even_count = 0
odd_count = 0
for i in range(n):
    if l[i] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("The number of even elements in the list is:", even_count)
print("The number of odd elements in the list is:", odd_count)