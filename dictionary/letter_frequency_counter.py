word=input("Enter a string of a word: ")
d1={}
for i in word:
    d1[i]=word.count(i)
print("The dictionary is:", d1)