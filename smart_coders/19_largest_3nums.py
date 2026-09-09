num1 = int ( input ("enetr the num : "))
num2 = int ( input ("enetr the num : "))
num3 = int ( input ("enetr the num : "))

if num1 > num2 and num2>num3 :
    print(f"{num1} is largest")

elif num2>num3:
    print(f"{num2} is largest")

else:
    print(f"{num3} is largest")