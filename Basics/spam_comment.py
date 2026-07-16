com=input("enter the comment: ")
spam=False
if "make a lot of money" in com:
    spam=True
elif "buy now" in com:
    spam=True
elif "click this" in com:
    spam=True
if spam:
    print("its spam")
else:
    print("not spam")