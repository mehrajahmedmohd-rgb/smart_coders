queue = []

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = int(input("Enter element: "))
        queue.append(item)
        print("Element inserted.")

    elif choice == 2:
        if len(queue) == 0:
            print("Queue Underflow")
        else:
            print("Deleted element:", queue.pop(0))

    elif choice == 3:
        if len(queue) == 0:
            print("Queue is empty")
        else:
            print("Queue:", queue)

    elif choice == 4:
        break

    else:
        print("Invalid Choice")