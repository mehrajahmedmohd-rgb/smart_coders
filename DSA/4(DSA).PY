def bubble(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


arr = list(map(int, input("enter the number :").split()))
re = bubble(arr)

print("sorted array[list] is", re)