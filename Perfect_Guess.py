'''Project 2 - The Perfecct Guess
We are going to write a program that generates a random number and asks user to guess it.
If the player's guess is higher than actual number, The program dispalys "Lower number please".Similarly if the user's guess is too low, the program prints "higher number please".
When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number
Hint:Use the random modulle
'''
import random


def perfect_guess_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    guess = None
    number_of_guesses = 0

    print("Welcome to 'The Perfect Guess' game!")
    print("I have selected a number between 1 and 100. Can you guess what it is?")

    while guess != number_to_guess:
        # Take user input
        guess = int(input("Enter your guess: "))
        number_of_guesses += 1

        # Check the user's guess and give hints
        if guess > number_to_guess:
            print("Lower number please.")
        elif guess < number_to_guess:
            print("Higher number please.")
        else:
            print(f"Congratulations! You've guessed the correct number: {number_to_guess}")
            print(f"You guessed it in {number_of_guesses} attempts.")


# Run the game
perfect_guess_game()