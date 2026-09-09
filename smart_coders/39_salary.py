sal = int (input("enter the overtime :"))

if sal <= 24:
    print(sal*1.5)

elif sal > 24 and sal <=40 :
    print(sal * 2)

else:
    print(sal * 4)