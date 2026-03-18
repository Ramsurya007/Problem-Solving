num1 = int(input("Enter a number 1"))
num2 = int(input("Enter a number 2"))
num3 = int(input("Enter a number 3"))
if num1 > num2 and num1> num3:
    print(num1)
elif num2 > num1 and num2> num3:
    print(num2)
elif num1 == num2 == num3:
    print ("All Equal")
else:
    print(num3)
