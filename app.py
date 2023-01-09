# Hangman
import random

words = ["elephant", "yellow", "Zimbabwe", "mountain", "circus"]
word_chosen = ""
num_letters = 0
wrong_guesses = []
right_guesses = []


def drawing():
    num_wrong_guesses = len(wrong_guesses)
    print("_ " * num_letters + "\n")
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
            print(" |    |")
            print("      |")
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


def user_guess():
    guess = input()


def game_initiation():
    word_chosen = random.choice(words)
    num_letters = len(word_chosen)
    # print(word_chosen)
    print("Welcome to Hangman.\n Choose a letter to start.")
    print("_ " * len(word_chosen))
    guess = input()


game_initiation()
