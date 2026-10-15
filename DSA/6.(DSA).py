def insert(arr):
  n = len(arr)
  for i in range(1,n):
    key = arr[i]
    j = i-1

    while j>=0 and arr[j] > key:
      arr[j+1] = arr[j]
      j = j - 1

    arr[j+1] = key 

  return arr

arr = list(map(int, input("Enter the numbers: ").split()))

result = insert(arr)

print("Sorted array is:", result)