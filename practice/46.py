def binary(arr,tar):
    l = 0
    h = len(arr)-1

    while l <= h :
        m = (l+h)//2

        if arr[m]==tar:
            return m

        elif arr[m]<tar:
            l = m+1

        else:
            h=m-1

    return -99

arr=[1,2,3,4,5,6]
tar=int(input("enter the number:"))
re = binary(arr,tar)
if re == -99:
    print("not")

else:
    print(re)