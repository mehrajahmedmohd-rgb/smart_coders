def linear(arr,tar):
    for i in range (len(arr)):
        if arr[i]==tar:
            return i

    return -99

arr=[1,2,3,4,5,6]
tar=int(input("enter the number:"))
re = linear(arr,tar)
if re == -99:
    print("not")

else:
    print(re)