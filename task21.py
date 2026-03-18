num =[int(x) for x in input("Enter a numbers").split(" ")]

for i in range(len(num)):
    for j in range(0,len(num)-1):
        if num[j]>num[j+1]:
            num[j],num[j+1]= num[j+1],num[j]
            print(num)
            
print(num)
