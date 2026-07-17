d1={}
while True:
    key1=input("Enter the key to be added to the dictionary: ")
    value1=input("Enter the value for the key: ")
    d1[key1]=value1
    choice=input("Do you want to add another key-value pair? (yes/no): ")
    if choice.lower() != 'yes':
        break
print(d1)
n= input("Enter the key you want to check: ")
count = 0
for i in d1:
    if i == n:
        count += 1
if count>0:
    print("The key is present in the dictionary.")
else:
    print("The key is not present in the dictionary.")
