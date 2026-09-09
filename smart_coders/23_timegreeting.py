hour = int ( input ("enter the hour :"))
if hour in range(5,11):
    print("good morning")

elif hour in range(12,17):
    print("good afternoon")

elif hour in range(18,20):
    print("good evening")

else:
    print("good night")