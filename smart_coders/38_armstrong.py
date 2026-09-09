num_str = input("Enter a 3-digit number: ")

d = int(num_str)
d1=int(num_str[0])
d2=int(num_str[1])
d3=int(num_str[2])

total = (d1**3)+(d2**3)+(d3**3)

if total == d:
    print("armstong")
else:
    print("not")

