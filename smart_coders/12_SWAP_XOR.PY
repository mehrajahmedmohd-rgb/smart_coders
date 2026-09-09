a=1
b=0
if bool(a) ^ bool(b) :
    a,b=b,a

else:
    print("not XOR")

print(a)
print(b)