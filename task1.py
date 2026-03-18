num = int(input("Enter a number"))
if num>0:
    print("Positive")
    if num%2==0:
        print("Even")
    else:
        print("odd")
elif num<0:
    print("negative")
else:
    print("Niethor")
