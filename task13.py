username = input("Enter the Username:")

if username == "admin":
    password =  input("Enter the Password:")
    if password == "admin@123":
        print("Login Successfully")
    else:
        print("Password is incorrect")
else:
    print("Username is incorrect")
    
