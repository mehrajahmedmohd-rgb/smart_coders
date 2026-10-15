def quick(arr):
    if len(arr)<=1:
        return arr

    pivot = arr[len(arr)//2]    

    l=[]
    m=[]
    r=[]

    for x in arr:
        if x<pivot:
            l.append(x)

        elif x == pivot:
            m.append(x)

        else:
            r.append(x)

    return quick(l)+quick(m)+quick(r)

arr = [5,2,7,1,8,3]
re = quick(arr)
print(re)
