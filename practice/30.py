health = 100

# The loop keeps running as long as health is greater than 0
while health > 0:
    print(f"Player is alive! Current health: {health}")
    
    # We take damage to prevent an infinite loop
    health = health - 20 

print("Game Over! You were knocked out.")
