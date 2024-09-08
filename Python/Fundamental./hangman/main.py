# Hangman in Python
from wordlist import words  # Import the list of words from an external file
import random  # Import the random module to select a random word

# Dictionary to store the hangman art for different stages of the game
hangman_art = {0: ("    ",
                   "    ",
                   "    "),
               1: ("  o  ",
                   "     ",
                   "     "),
               2: ("  o  ",
                   "  |  ",
                   "     "),
               3: ("  o  ",
                   " /|  ",
                   "     "),
               4: ("  o  ",
                   " /|\\ ",
                   "     "),
               5: ("  o  ",
                   " /|\\ ",
                   " /   "),
               6: ("  o  ",
                   " /|\\ ",
                   " / \\ ")}

# Function to display the current state of the hangman
def display_man(wrong_guesses):
    print("**********")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("**********")

# Function to display the current hint (partially guessed word)
def display_hint(hint):
    print(" ".join(hint))

# Function to display the final answer (fully guessed word)
def display_answer(answer):
    print(" ".join(answer))

# Main function to run the game
def main():
    answer = random.choice(words)  # Select a random word from the word list
    hint = ["_"] * len(answer)  # Create a hint with underscores for each letter in the answer
    wrong_guesses = 0  # Initialize the count of wrong guesses
    guessed_letters = set()  # Set to keep track of guessed letters
    is_running = True  # Flag to keep the game running

    while is_running:
        display_man(wrong_guesses)  # Display the current state of the hangman
        display_hint(hint)  # Display the current hint
        guess = input("Enter a letter: ").lower()  # Get a letter guess from the user

        # Check if the input is valid (a single alphabetic character)
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)  # Add the guessed letter to the set

        # Check if the guessed letter is in the answer
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess  # Update the hint with the correctly guessed letter
        else:
            wrong_guesses += 1  # Increment the wrong guess count

        # Check if the player has guessed the entire word
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False
        # Check if the player has reached the maximum number of wrong guesses
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You Lose!")
            is_running = False

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
