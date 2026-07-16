m1=int(input("Enter marks for first subject: "))
m2=int(input("Enter marks for second subject: "))
m3=int(input("Enter marks for third subject: "))
if (m1+m2+m3)>0.4*300:
    if m1>0.3*100:
        print("passed in first subject")
    else:
        print("failed in first subject")
    if m2>0.3*100:
        print("passed in second subject")
    else:
        print("failed in second subject")
    if m3>0.3*100:
        print("passed in third subject")
    else:
        print("failed in third subject")
    if m1>0.3*100 and m2>0.3*100 and m3>0.3*100:
        print("passed in all three subjects")
else:
    print("failed")