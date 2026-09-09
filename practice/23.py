import time

n=input("set password:")

if n=="1234567890":
    print("accecing password")
    time.sleep(1)
    print("wait processing....")

    time.sleep(2)
    print("creating password")
    print("created successfully")

    time.sleep(1)
    print(n)

else:
            print("accecing password")
            time.sleep(1)
            print("wait processing....")

            time.sleep(2)
            print("creating password")
            print("not created")

            time.sleep(1)   
            print("password is not created try again..")


import secrets
import string

length = 12

characters = string.ascii_letters + string.digits + string.punctuation

password = "".join(secrets.choice(characters) for _ in range(length))

print("Secure Password:", password)            
 