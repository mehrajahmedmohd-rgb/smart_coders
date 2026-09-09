a = int(input("enter the side 1:"))
b = int(input("enter the side 2:"))
operator = input ("enter the condition : ")

match operator:
    case '+' :
        print("addition = ", a+b)

    case '-':
        print("subraction =",a-b)

    case '*':
        print("multiplication =" ,a*b)
     
    case '/':
        if a==0 or b ==0:
            print("0")

        else:
            print("division =",a/b)

