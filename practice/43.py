def lin(arr,tar):
    for i in range(len(arr)):
        if arr[i]==tar:
            return i

    return -19

arr=list(map(int , input("enter the elements :").split()))
tar=int(input("enter the target elemnet :"))            

res = lin(arr,tar)

if res==-19:
    print("not found.... try again")

else :
    print("found at index",res)    