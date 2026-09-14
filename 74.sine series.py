x = float(input("Enter x: "))
n = int(input("Enter number of terms: "))

total = 0

for i in range(n):
    power = 2 * i + 1

    factorial = 1
    for j in range(1, power + 1):
        factorial *= j

    term = (x ** power) / factorial

    if i % 2 == 0:
        total += term
    else:
        total -= term

print("Sum:", total)