n= input("Enter a string:")
lst=n.split()
d1={}
for i in lst:
    d1[i]=lst.count(i)
print("The dictionary is:", d1)
for i in d1:
    print("The frequency of",i,"is:",d1[i])