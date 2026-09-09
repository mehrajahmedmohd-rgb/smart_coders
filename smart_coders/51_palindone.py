n = int (input ("enter the number :"))
rev = 0
temp = n

while temp > 0 :

    digit = n%10
    rev = rev * 10 + digit 
    n = n//10

if rev == n:
    print("palindrone")

else:
    print("not palindrone")