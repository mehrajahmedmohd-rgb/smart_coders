a = int(input("enter the number :"))

if a > 1:
    print("positive")

    if a % 2 == 0 :
        print("even")
    else:
        print("odd")

elif a<0:
    print("negative")

else:
    print("zero")

