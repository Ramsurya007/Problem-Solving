num = int(input("Enter a number"))
if num == 0 or num == 1:
    print("Neither prime or Non-Prime")
else:
    for i in range(2,num):
        if num%i==0  :
            print("Not Prime")
            break  
    else:
            print("Prime")
            
            
            
