num1 = int(input("Enter a number:"))
choice = input("Enter a operator like (+,-,*,/):")
num2 = int(input("Enter a number"))
match choice:
    case '+':
        print(num1+num2)
    case '-':
        print(num1-num2)
    case '*':
        print(num1*num2)
    case '/':
        print(num1/num2)
    case _:
        print("Enter a correct operator")
    
