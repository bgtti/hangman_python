# Hangman game
import random

words = ["elephant", "yellow", "Zimbabwe", "mountain", "circus"]
word_chosen = []
word_printed = []
num_letters = 0
wrong_guesses = []


def the_game_loop():
    global word_chosen
    word_chosen = []
    global word_printed
    word_printed = []
    global wrong_guesses
    wrong_guesses = []
    game_initiation()


def replay():
    print("Would you like to play again?")
    print("Type 'replay' to play again or 'exit' to stop.")
    replay_answer = input()
    if replay_answer == "replay":
        print("***New game started***\n")
        the_game_loop()
    else:
        print("***Thank you for playing, goodbye!***\n")


def check_game():
    if len(wrong_guesses) == 6:
        print("***** Game over: you lose! *****\n")
        replay()
    elif word_chosen == word_printed:
        print("***** Game over: you win! *****\n")
        replay()
    else:
        game()


def game():
    print("Guess a letter: ")
    guess = input()
    if guess in word_chosen or guess.lower() in word_chosen or guess.upper() in word_chosen:
        for i in range(num_letters):
            if guess.lower() == word_chosen[i].lower():
                global word_printed
                word_printed[i] = word_chosen[i]
    else:
        wrong_guesses.append(guess.lower())
    drawing()


def drawing():
    print("===========================")
    num_wrong_guesses = len(wrong_guesses)
    print(" ".join(word_printed))
    print()
    if num_wrong_guesses > 0:
        print("Your wrong guesses: " + ', '.join(wrong_guesses))
    print(" +---+")
    print(" |   |")
    if num_wrong_guesses > 0:
        print(" O   |")
        if num_wrong_guesses == 1:
            print("     |")
            print("     |")
        elif num_wrong_guesses == 2:
            print(" |   |")
            print("     |")
        elif num_wrong_guesses == 3:
            print("/|   |")
            print("     |")
        elif num_wrong_guesses == 4:
            print("/|\  |")
            print("     |")
        elif num_wrong_guesses == 5:
            print("/|\  |")
            print("/    |")
        elif num_wrong_guesses == 6:
            print("/|\  |")
            print("/ \  |")

    else:
        print("     |")
        print("     |")
        print("     |")

    print("     |")
    print()
    check_game()


def game_initiation():
    global word_chosen
    word_chosen = list(random.choice(words))
    global num_letters
    num_letters = int(len(word_chosen))
    for i in range(num_letters):
        word_printed.append("_")
    print("===========================")
    print("\n*  Welcome to Hangman.  *\nGuess a letter to start.\n")
    drawing()


the_game_loop()
