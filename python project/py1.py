import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Choose a difficulty level:")
    print("Easy: Guess a number between 1 and 50.")
    print("Medium: Guess a number between 1 and 100.")
    print("Hard: Guess a number between 1 and 200.")

    # Choose difficulty level
    level = input("Enter difficulty level (Easy, Medium, Hard): ").lower()
    if level == "easy":
        max_number = 50
        max_attempts = 10
    elif level == "medium":
        max_number = 100
        max_attempts = 7
    elif level == "hard":
        max_number = 200
        max_attempts = 5
    else:
        print("Invalid difficulty level. Defaulting to Medium.")
        max_number = 100
        max_attempts = 7

    # Generate a random number based on the difficulty level
    secret_number = random.randint(1, max_number)
    attempts = 0

    print(f"\nI am thinking of a number between 1 and {max_number}. Can you guess what it is?")
    print(f"You have {max_attempts} attempts to guess correctly.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts!")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

        # Check if attempts are exhausted
        if attempts == max_attempts:
            print(f"Game over! You've used all {max_attempts} attempts. The number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()
