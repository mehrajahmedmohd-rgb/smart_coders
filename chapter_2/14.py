'''Create a program that:
takes name (string) and age (int)
converts age into string

concatenates both and prints a message like:

"My name is John and I am 20 years old"'''

name=str(input("enter name:"))
age=int(input("enter age :"))

age=str(age)
p=type(name) , type(age)
print(p)

print(f"my name is {name} and iam {age} years old")