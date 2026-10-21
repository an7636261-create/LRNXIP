"""
Number Guessing Game
Learnix Week 1 - Python Intern

The computer chooses a random number between 1 and 100.
The player tries to guess the number with a limited number of attempts.
"""

import random


def play_game():
    """Run one round of the number guessing game."""
    secret_number = random.randint(1, 100)
    attempts_left = 7

    print("\n=== Number Guessing Game ===")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {attempts_left} attempts to guess it.")

    # Keep asking until the player guesses correctly or runs out of attempts.
    while attempts_left > 0:
        try:
            guess = int(input("\nEnter your guess: "))
        except ValueError:
            # Handle text or other input that cannot be converted to an integer.
            print("Please enter a whole number, such as 42.")
            continue

        # Check the allowed range before comparing the guess.
        if guess < 1 or guess > 100:
            print("Your guess must be between 1 and 100.")
            continue

        attempts_left -= 1

        if guess == secret_number:
            attempts_used = 7 - attempts_left
            print(f"Correct! The number was {secret_number}.")
            print(f"You guessed it in {attempts_used} attempt(s).")
            return

        if guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

        print(f"Attempts remaining: {attempts_left}")

    # This runs only when the player uses all valid attempts without winning.
    print(f"Game over! The number was {secret_number}.")


def main():
    """Show the menu and let the player replay or exit."""
    print("Welcome to the Number Guessing Game!")

    while True:
        play_game()

        # Ask whether the player wants to start another round.
        while True:
            play_again = input("\nWould you like to play again? (y/n): ").strip().lower()
            if play_again in ("y", "n"):
                break
            print("Please enter 'y' for yes or 'n' for no.")

        if play_again == "n":
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()
