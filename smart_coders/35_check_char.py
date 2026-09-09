c = input ("enter the character :")

if len(c) != 1:
    print("enter one char")

elif c.isalpha():
    print("alphabet")

elif c.isdigit():
    print("digit"
    )

else:
    print("special char")