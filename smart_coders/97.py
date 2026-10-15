n = 5
num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num + j * n, end=" ")
    num += 1
    print()