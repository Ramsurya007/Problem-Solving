num = int(input("Enter a number"))
num1 = num
rev = 0
while num!=0:
    temp = num%10
    rev = temp +rev*10
    num = num//10

if num1==rev:
    print("Palindrome")
else:
    print("Not Palindrome")
