"""
Hangman Game
------------
A simple text-based Hangman game.
The player guesses letters one at a time to reveal a hidden word.
The player loses if they make 6 incorrect guesses.
"""

import random  # used to randomly pick a word from our list


def choose_word(word_list):
    """Randomly select one word from the given list of words."""
    return random.choice(word_list)


def display_word(word, guessed_letters):
    """
    Build and return the current state of the word to display.
    Each letter that has been guessed is shown; others are shown as '_'.
    """
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "   # show the letter if it's been guessed
        else:
            display += "_ "           # hide the letter otherwise
    return display.strip()


def play_hangman():
    # Step 1: Predefined list of words to choose from
    word_list = ["python", "hangman", "computer", "keyboard", "program"]

    # Step 2: Randomly choose the secret word
    secret_word = choose_word(word_list)

    # Step 3: Set up game variables
    guessed_letters = []       # letters the player has already guessed
    max_incorrect = 6          # maximum allowed wrong guesses
    incorrect_guesses = 0      # counter for wrong guesses

    print("Welcome to Hangman!")
    print("Try to guess the word one letter at a time.")
    print("You have", max_incorrect, "incorrect guesses allowed.\n")

    # Step 4: Main game loop — continues until the player wins or loses
    while incorrect_guesses < max_incorrect:

        # Show the current state of the word
        print("Word:", display_word(secret_word, guessed_letters))
        print("Guessed letters:", guessed_letters)
        print("Remaining attempts:", max_incorrect - incorrect_guesses)

        # Get input from the player
        guess = input("Enter a letter: ").lower()

        # Basic input validation: must be a single alphabet letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.\n")
            continue  # skip the rest of the loop and ask again

        # Check if the letter was already guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.\n")
            continue

        # Add the new guess to the guessed_letters list
        guessed_letters.append(guess)

        # Check if the guessed letter is in the secret word
        if guess in secret_word:
            print("Good guess!\n")
        else:
            incorrect_guesses += 1
            print("Wrong guess!\n")

        # Step 5: Check if the player has revealed the entire word (Win condition)
        # This works by checking if every letter in secret_word is in guessed_letters
        word_complete = True
        for letter in secret_word:
            if letter not in guessed_letters:
                word_complete = False
                break

        if word_complete:
            print("Word:", display_word(secret_word, guessed_letters))
            print("You Win! The word was:", secret_word)
            return  # end the game immediately since the player won

    # Step 6: If the loop ends because incorrect_guesses reached max_incorrect, player loses
    print("Game Over! You've used all", max_incorrect, "incorrect guesses.")
    print("The correct word was:", secret_word)


# Step 7: Run the game only if this file is executed directly
if __name__ == "__main__":
    play_hangman()
