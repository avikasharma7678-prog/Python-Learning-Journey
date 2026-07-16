names=input("Enter names:")
l1=names.split()
for i in l1:
    if i[0] in "Ss":
         print("Hello! "+i)
    else:
        continue
