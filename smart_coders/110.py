n = 5

for i in range(2 * n - 1):
    row = i if i < n else 2 * n - 2 - i

    for j in range(2 * n - 1):
        if j == n - 1 - row or j == n - 1 + row:
            print("*", end="")
        else:
            print(" ", end="")

    print()