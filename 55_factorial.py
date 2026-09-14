n = int (input("enetr the num : "))
fact = 1

if n < 0 :
    print("not exist ")

elif n == 0:
    print("fact of zero is one")

else:
    for i in range (1,n+1):
        fact = fact *i

    print(f"factorial of {n} is {fact}")