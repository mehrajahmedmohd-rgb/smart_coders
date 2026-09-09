id = 126
password = "mehraj111"

a = int ( input ("enter the id :"))
b=input("enter the password :"
        )
if id == a and password == b :
    print("login successfully in your account ...")

elif id == a and password != b :
    print("incorrect password ...")

elif id != a and password ==b:
    print("invalid id")

else:
    print("error id and password not found ")
    print("TRY AGAIN ...")
