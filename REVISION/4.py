n = int(input("enter :"))


if n < 0 or n > 100:
  print("Invalid marks! Please enter a number between 0 and 100.")

elif n >= 90:
    print("A GRADE")

elif n >= 75 and n<90:
    print("B GRADE")

elif n >= 60 and n <75:
    print("C GRADE ")

elif n >= 40 and n<60:
    print("D GRADE")

else:
    print("FAIL ")