str1=input("Enter the string:")
str2=""
count=1
for i in range(len(str1)-1):
    if str1[i+1] == str1[i]:
        count +=1
    else:
        str2 += str1[i]+str(count)
        count=1
str2=str2 + str1[-1] +str(count)
print("The compressed string is:", str2)