'''  Try writing the code for Question 2 (The ATM Withdrawal):
Set balance = 10000.
Ask for a pin = int(input("Enter PIN: ")).
If the pin is 1234, then ask for the amount. 
Inside that same block, 
check if they have enough balance.Else, 
print "Wrong PIN". '''

set=10000
pin = int(input("Enter PIN: "))

if pin==1234:
    print("correct pin")
    amount = int(input("Enter the amount to withdraw: "))
    if amount<=set:
        print("amount withdraw successfully.. ")
    else:
         print("check if they have enough balance")

else:
    print("incorrect pin")         
