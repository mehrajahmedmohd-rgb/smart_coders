n = int (input("enter the number:"))
fact = 1

if n < 0 :
    print("the factorial of negetive is not exist")

elif n==0:
    print("factorial of zero is 1")

else:
    for i in range (1,n+1):
        fact = fact * i
print(fact)
