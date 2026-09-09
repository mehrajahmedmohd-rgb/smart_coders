cost = int(input("Enter the cost price: "))
sell = int(input("Enter the selling price: "))

profit = sell - cost 

if profit > 0:
    print(f"Profit made! The profit is: {profit}")

elif profit < 0:
    print(f"Loss taken! The loss is: {profit * -1}")

else:
    print("No loss or profit (You broke even).")
