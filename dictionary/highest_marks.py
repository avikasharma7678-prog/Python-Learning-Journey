d1={}
n=int(input("Enter the number of key-value pairs you want to add to the dictionary: "))
for i in range(n):
    key1=input("Enter the name of the studentto be added to the dictionary: ")
    value1=int(input("Enter the marks for the student: "))
    d1[key1]=value1
print("The dictionary is:", d1)
lst=list(d1.keys())
highest=lst[0]
for i in lst:
    if i > highest:
        highest = i
print("The highest marks are:", highest,d1[highest])