sr= input("Enter a string:")
str1=""
for i in range(len(sr)-1):
    if sr[i+1].isnumeric() and sr[i].isalpha():
        str1 += sr[i]*(int(sr[i+1]))
    elif sr[i].isnumeric():
        continue
    else:
        str1 += sr[i]
if sr[-1].isalpha():
    str1 += sr[-1]
print("The expanded string is:", str1)