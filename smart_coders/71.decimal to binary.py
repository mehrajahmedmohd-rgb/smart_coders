n = int(input("Enter decimal number: "))

if n == 0:
    print("Binary: 0")
else:
    binary = ""

    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n //= 2

    print("Binary:", binary)