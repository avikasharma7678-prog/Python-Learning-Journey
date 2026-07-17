d1={}
n=int(input("Enter the number of key-value pairs you want to add to the dictionary: "))
for i in range(n):
    key1=input("Enter the name to be added to the dictionary: ")
    value1=int(input("Enter the marks for the key: "))
    d1[key1]=value1
print("The dictionary is:", d1)
total = sum(d1.values())
avg=total/n
print("The average of the values in the dictionary is:", avg)