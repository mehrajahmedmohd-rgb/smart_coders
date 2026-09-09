fixed_charge = 100
unit = int (input ("enter the units ..."))

if unit <=100:
    print("the price is " , unit*1.50)

elif unit <= 300:
    print("the price is " , (100 * 1.50) + ((unit - 100) * 2.50))

else:
    print("the price is " , (100 * 1.50) + (200 * 2.50) + ((unit - 300) * 4.00))
    