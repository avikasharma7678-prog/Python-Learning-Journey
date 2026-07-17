students={}
d1={}
while True:
    name=input("Enter the name of the student(enter 'exit' to stop): ")
    if name == "exit":
        break
    else:
        class1=input("Enter the class of the student: ")
        age=int(input("Enter the age of the student: "))
        marks=int(input("Enter the marks of the student: "))
        d1["Name"]=name
        d1["Class"]=class1
        d1["Age"]=age
        d1["Marks"]=marks
        roll_no=int(input("Enter the roll number of the student: "))
        students[roll_no]=d1
print("The student database is:", students)    