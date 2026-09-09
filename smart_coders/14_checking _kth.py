n = int(input("enter the number :")) 


k = int(input("enter the number :"))

mask = 1 << k
if (n & mask) == 0:
    print(f"Bit at position {k} is 0")
else:
    print(f"Bit at position {k} is 1")
