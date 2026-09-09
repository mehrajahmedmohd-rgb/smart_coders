# Take number from user
num = int(input("Enter number: "))

# Outer loop for rows
for i in range(1,num+1):

    # Inner loop for printing #
    for j in range(1, i + 1):
        print("*", end=" ")

    # Move to next line
    print()