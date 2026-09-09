secret_number = 7
guess = 0  # Starting at 0 ensures the loop begins

# The loop keeps running as long as the guess is NOT 7
while guess != secret_number:
    guess = int(input("Guess the secret number: "))
    
    if guess != secret_number:
        print("Wrong guess! Try again.")

# Once the loop ends (because guess == 7), this line runs
print("You won the match! 🎉")

