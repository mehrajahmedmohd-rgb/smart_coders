n = int (input ("enter the number :"))

total = 0

while n>0:
    total += n % 10
    n = n // 10
    

print(total)