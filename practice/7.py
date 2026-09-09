#swap two numbers

num1=int(input("enter the 1st number:"))
num2=int(input("enter the 2nd number:"))
print("***before swap ***")
print(num1,num2)

temp=num1
num1=num2
num2=temp

print("***after swap***")
print(num1,num2)