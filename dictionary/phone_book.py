d1={}
while True:
    choice=int(input("Enter your choice:\n1. Add contact\n2. Search contact\n3. Display all\n4.Delete Contact\n5. Exit\n"))
    if choice == 1:
        name=input("Enter the name of the contact: ")
        number=input("Enter the phone number of the contact: ")
        d1[name]=number
        print("The contact has been added to the phone book.")
    elif choice == 2:
        name=input("Enter the name of the contact to search: ")
        if name in d1:
            print("The phone number of",name,"is:",d1[name])
        else:
            print("Contact not found.")
    elif choice == 3:
        print("The phone book contains the following contacts:")
        for name in d1:
            print(name, d1[name])
    elif choice == 4:
        name=input("Enter the name of the contact to delete: ")
        if name in d1:
            del d1[name]
            print("The contact has been deleted from the phone book.")
        else:
            print("Contact not found.")
    elif choice == 5:
        exit()
    else:
        print("Invalid choice. Please try again.")
