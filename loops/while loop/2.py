num=454
rev=0
temp=num
while temp>0:
    d=temp%10
    rev=rev*10+d
    temp=temp//10
if rev==num:
    print("palin")

else:
    print("not palin")    



