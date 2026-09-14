a = int (input("enter the number :"))
b = int (input("enter the number :"))

num1 = a 
num2 = b 



while b!=0:
    a,b = b,a%b
gcd = a

lcm = (num1*num2)//gcd
print(lcm)