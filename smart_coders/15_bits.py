n = int(input("enter the number :")) 


for i in range (1,n):
    print(i)

    
mask = 1 << k
if (n & mask) == 0:
    print(f"Bit at position {k} is 0")
else:
    print(f"Bit at position {k} is 1")


