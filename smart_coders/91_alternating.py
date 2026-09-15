n = int ( input ("enter the number: "))


for i in range(1,n+1):
    for j in range(1,i+1):
        if j % 2 == 0:
            num = 0
        else:
            num = 1
        print( num , end=" ")     

    print()