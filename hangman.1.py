import random

# Hangman stages
HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]

# Select a random word
def choose_word():
    try:
        with open("words.txt", "r", encoding="utf-8") as file:
            words = [
                word.strip().lower()
                for word in file
                if word.strip().isalpha()
            ]
        if words:
            return random.choice(words)
    except FileNotFoundError:
        pass

    words = ["python", "computer", "programming",
             "network", "keyboard", "software"]

    return random.choice(words)


# Display hidden word
def display_word(word, guessed_letters):
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in word
    )


# Main game
def play_game():

    print("Welcome to Hangman Game!")
    print("Let's start playing!")

    word = choose_word()
    guessed_letters = set()
    attempts = 6

    while attempts > 0:

        print(HANGMAN_PICS[6 - attempts])
        print("\nWord:", display_word(word, guessed_letters))
        print("Guessed letters:", sorted(guessed_letters))
        print("Attempts left:", attempts)

        guess = input("\nGuess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct guess!")
        else:
            print("Wrong guess!")
            attempts -= 1

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You won!")
            print("The word was:", word)
            return

    print(HANGMAN_PICS[6])
    print("\nGame Over! You lost.")
    print("The correct word was:", word)


# Run game
if __name__ == "__main__":
    play_game()