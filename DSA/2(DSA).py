def linear(arr,tar):
    for i in range(len(arr)):
        if arr[i]==tar:
            return i
    return -2

arr = list(map(int, input("Enter numbers: ").split()))            
tar=int(input("enter the target element:"))

found=linear(arr,tar)

if found!=-2:
   print("found at index",found)

else:
    print("not found the element in list")
