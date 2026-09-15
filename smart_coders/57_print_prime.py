N = 10  
num = 2  
count = 0

while count < N:
   
    for i in range(2, num):
        if num % i == 0:
            break 
    else:
        print(num, end=" ")
        count += 1

    num += 1  
