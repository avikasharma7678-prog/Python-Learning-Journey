d1={}
while True:
    key1=input("Enter the key to be added to the dictionary: ")
    value1=input("Enter the value for the key: ")
    d1[key1]=value1
    choice=input("Do you want to add another key-value pair? (yes/no): ")
    if choice.lower() =='no':
        break
print("The dictionary is:", d1)
for i in d1:
    print(i, ":", d1[i])