# Hangman
import random

words = ["elephant", "yellow", "Zimbabwe", "mountain", "circus"]


def game_initiation():
    word_chosen = random.choice(words)
    # print(word_chosen)
    print("Welcome to Hangman.\n Choose a letter to start.")
    print("_ " * len(word_chosen))


game_initiation()
