#------- for intergers / numbers ---------

num = int(input("enter the number:"))
rev = 0 
temp = num 

while temp>0 :
    digit = temp % 10
    rev = rev * 10 + digit 
    temp = temp // 10

if rev == num :
    print("palindrome")

else:
    print("not palindrome")        


# ------ for characters / names ------

num_1 = input("enter the name:") 

if num_1== num_1[::-1] :
    print("palindrome")

else:
    print("not palindrome")    


