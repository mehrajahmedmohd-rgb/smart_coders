def factorial(num):
    fact = 1
    if num == 0:
        print("not defined")

    elif num==0 :
        print("factorial of zero is 1")

    else:
        for i in range(1,num+1):
          fact = fact * i  

    print(f"factorioal of {num} is {fact}")


num= int(input("enter the number"))            
factorial(num)