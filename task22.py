contact={}
while True:
    choice = int(input("Enter Your Chocie: \n 1. ADD Contact \n 2.Display all Contact \n 3. Search by Name \n 4.Exit"))
    match choice:
        case 1:
            name = input("Enter a name:")
            number = input("Enter a Number:")
            contact[name]= number
        case 2:
            if not contact:
                print("Please Enter the Contact First")
            else:
                print(contact)
        case 3:
            if not contact :
                print("Please Enter the Contact First")
            else:
                name1 = input("Enter a name to search:")
                if name1 in contact.keys():
                    print(f"Name:{name1}-> Number: {contact[name1]}")
                else:
                    print("No contact in that name ")
        case 4:
            break
        case _ :
            print("Only Enter vaild number showed in display")
            
            
