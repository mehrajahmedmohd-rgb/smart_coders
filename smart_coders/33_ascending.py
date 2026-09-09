a = int (input("enter the num :"))
b = int (input("enter the num :"))
c = int (input("enter the num :"))

s = 0
m = 0
l = 0

if a<=b and a<=c :
    s = a
    if b<=c:
        m=b
        l=c

    else:
        m=c
        l=b


elif b<=a and b<=c:
    s = b
    if a<=c:
        m=a
        l=c
    else:
        m=c
        l=a

else:
    s = c
    if a<=b:
        m=a
        l=b
    else:
        m=b
        l=a

print(s,m,l)