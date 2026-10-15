n = 13

for i in range(3):
    for j in range(n):
        if ((i + 1) % 2 == 1 and j % 4 == 0) or \
           ((i + 1) % 2 == 0 and j % 2 == 0 and j % 4 != 0):
            print("*", end="")
        else:
            print(" ", end="")
    print()