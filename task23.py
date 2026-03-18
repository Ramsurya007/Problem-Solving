def add_contact():
    with open('contact.txt','a+') as f :
        name = input("Enter a Name:")
        number = input("Enter a Number:")
        f.write(f'{name}-{number}\n')

def display_contact():
    with open('contact.txt','r+') as f :
        for i in f:
            name, number =i.split('-')
            print(f'Name:{name} -> Number:{number}')

while True:
    choice = int(input("Enter a choice:\n 1. Add Contact \n 2. Display Contact \n 3. Exit"))
    match choice:
        case 1:
            add_contact()
        case 2:
            display_contact()
        case 3:
            break
        case _ :
            print("Only Enter valid number showed in display")
