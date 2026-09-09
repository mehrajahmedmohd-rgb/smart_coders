n = int(input("Enter number: "))

seen = set()

while n != 1 and n not in seen:
    seen.add(n)
    total = 0

    while n > 0:
        digit = n % 10
        total += digit * digit
        n //= 10

    n = total

if n == 1:
    print("Happy Number")
else:
    print("Not a Happy Number")