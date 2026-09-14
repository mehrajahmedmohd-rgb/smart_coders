total = 0
count = 0

while True:
    n = float(input("Enter number (-1 to stop): "))

    if n == -1:
        break

    total += n
    count += 1

if count > 0:
    average = total / count
    print("Count:", count)
    print("Average:", average)
else:
    print("No numbers entered")