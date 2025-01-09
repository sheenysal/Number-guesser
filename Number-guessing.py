import random

def number_guessing_game():
    #A simple number guessing game where the player guesses a number within a range.
    print("Welcome to the Number Guessing Game!")

    # Set the range for the random number
    lower_bound = 1
    upper_bound = 100
    random_number = random.randint(lower_bound, upper_bound)

    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}. Can you guess what it is?")

    attempts = 0

    while True:
        # Get user's guess
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue

        attempts += 1

        # Check the guess
        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break

    # Ask if the player wants to play again
    play_again = input("Would you like to play again? (yes/no): ").lower()
    if play_again == "yes":
        number_guessing_game()
    else:
        print("Thanks for playing! Goodbye!")


# Run the game
if __name__ == "__main__":
    number_guessing_game()
