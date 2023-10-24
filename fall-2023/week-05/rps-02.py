import random

arr = ['scissors', 'rock', 'paper']

player_health = 10
enemy_health = 10

while player_health > 0 and enemy_health > 0:
    print(f"Player health: {player_health}, Enemy health: {enemy_health}")

    p1 = input("Enter rock, paper, or scissors: ")
    p2 = random.choice(arr)

    print(f"Player chose {p1}, Enemy chose {p2}")

    if p1 == "rock" and p2 == "scissors":
        print("Rock vs Scissors - Player wins!")
        enemy_health -= 1
    elif p1 == "paper" and p2 == "scissors":
        print("Paper vs Scissors - Enemy wins!")
        player_health -= 1
    elif p1 == "scissors" and p2 == "scissors":
        print("Scissors vs Scissors - It's a tie!")
    elif p1 == "rock" and p2 == "paper":
        print("Rock vs Paper - Enemy wins!")
        player_health -= 1
    elif p1 == "paper" and p2 == "paper":
        print("Paper vs Paper - It's a tie!")
    elif p1 == "scissors" and p2 == "paper":
        print("Scissors vs Paper - Player wins!")
        enemy_health -= 1
    elif p1 == "rock" and p2 == "rock":
        print("Rock vs Rock - It's a tie!")
    elif p1 == "paper" and p2 == "rock":
        print("Paper vs Rock - Player wins!")
        enemy_health -= 1
    elif p1 == "scissors" and p2 == "rock":
        print("Scissors vs Rock - Enemy wins!")
        player_health -= 1
    else:
        print("Invalid input")

# Determine the winner
if player_health <= 0:
    print("Player has run out of health. Enemy wins!")
elif enemy_health <= 0:
    print("Enemy has run out of health. Player wins!")
