
num = int(input("Enter a number"))
num1 = num
arm = 0
while num!=0:
    temp = num%10
    arm += temp**3
    num = num//10
if num1 == arm:
    print("It's Armstrong")
else :
    print("It's not Armstrong")
