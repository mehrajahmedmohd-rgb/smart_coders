x = int(input("enter the number :"))
y = int(input("enter the number :"))

if x >= 0 and y >= 0:
    print("1st quadrant")

elif x<0 and y<0 :
    print("3rd quadrant")

elif x>=0 and y<0:
    print("4th quadrant")

else:
    print("2nd quadrant")