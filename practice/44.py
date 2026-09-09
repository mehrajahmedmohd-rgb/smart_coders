def binary(arr,tar):
    
    l = 0 
    r= len(arr)-1

    while l <= r:
        m = l +(r-l)//2

        if arr[m]==tar:
            return m

        elif arr[m]<tar:
            l = m + 1

        else:
            r = m - 1

    return -99


arr=list(map(int , input("enter the list :").split()))
tar=int(input("enter the target element from list... :"))

re = binary(arr,tar)

if re == -99:
    print("not found try again ..... ")

else:
    print("founded at index ", re)

