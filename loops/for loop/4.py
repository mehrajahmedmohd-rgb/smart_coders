n=int(input("enter the number:"))
for i in range(1,n+1):
    # in this loop printing or decreacing nums or printing space
    for j in range(n-i):
        print(" ",end=" ")

    #printing colums
    for k in range(2*i-1):
        print(i,end=" ")
    # Move to next line    
    print()    