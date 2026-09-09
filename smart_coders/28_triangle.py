a = float (input("enter the side 1:"))
b = float (input("enter the side 2:"))
c = float (input("enter the side 3:"))

unique_remove=len({a,b,c}) # len(5,5,5) = 5,5,5

if unique_remove == 1:
    print("equilateral triangle")

elif unique_remove == 2 : #len(5,5,7) = 5,7
    print("iosoceles triangle")

else:
    print("scalene triangle")