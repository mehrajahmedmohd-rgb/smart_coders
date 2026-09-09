a = int ( input ("enter the num :"))
b = int ( input ("enter the num :"))
c = int ( input ("enter the num :"))


if a == b & b == c  :
    print("all equal")

elif a==b & b!=c:
    print("2 equal")

elif a!=b & b==c:
    print("2 equal")

elif a==c:
    print("2 equal")

else:
    print("not equal")