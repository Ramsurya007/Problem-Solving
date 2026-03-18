num = int(input("Enter a number"))
count = 0
while num!=0:
    temp = num%10
    count += temp
    num = num//10

print(count)
