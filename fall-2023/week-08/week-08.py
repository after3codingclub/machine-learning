import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    while True:
        # Get user input and handle non-numeric input
        try:
            guess = int(input("Guess the number between 1 and 100: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        # Check if the guess is correct
        if guess == secret_number:
            print("Congratulations! You guessed the correct number.")
            break
        elif guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

if __name__ == "__main__":
    guess_number()
