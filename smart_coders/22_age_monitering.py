A=int(input("enter the age of the person ...  :"))

if A<18:
    print("the person is child..")

elif A>=18 and A<25:
    print("the person is teenager..")

elif A>=25 and A<50:
    print("the person is adult..")

elif A>50 and A<=99:
    print("the person is senior citizens..")

else:
    print("the person is centery man ..")