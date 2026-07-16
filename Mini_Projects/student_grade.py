marks=float(input("Enter your marks to get grades:"))
if marks>100:
    print("Enter valid marks:")
elif 90<=marks<=100:
    print("A+")
elif 85<=marks<=89:
    print("A")
elif 80<=marks<=84:
    print("A-")
elif 75<=marks<=79:
    print("B+")
elif 70<=marks<=74:
    print("B")
elif 65<=marks<=69:
    print("C+")
elif 60<=marks<=64:
    print("C")
elif 55<=marks<=59:
    print("D+")
elif 50<=marks<=54:
    print("D")
elif 45<=marks<=49:
    print("E")
else:
    print("F")