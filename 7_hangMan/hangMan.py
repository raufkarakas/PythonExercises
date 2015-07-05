__author__ = 'rkarakas'

import random

def hangMan():
    pictures = ["""
                   +---+
                   |   |
                       |
                       |
                       |
                       |
                =========""","""
                   +---+
                   |   |
                   O   |
                       |
                       |
                       |
                =========""","""
                   +---+
                   |   |
                   O   |
                   |   |
                       |
                       |
                =========""","""
                   +---+
                   |   |
                   O   |
                  /|   |
                       |
                       |
                =========""","""
                   +---+
                   |   |
                   O   |
                  /|\  |
                       |
                       |
                =========""","""
                   +---+
                   |   |
                   O   |
                  /|\  |
                  /    |
                       |
                =========""","""
                   +---+
                   |   |
                   O   |
                  /|\  |
                  / \  |
                       |
                ========="""]

    word = random.choice(["python", "linux", "coding", "programming"])
    guessList = []
    state = 0

    while state <= 5:
        hiddenWord = ""
        for c in word:
            if c in guessList:
                hiddenWord += c
            else:
                hiddenWord += " _ "
        print(hiddenWord)
        print(pictures[state])
        userGuess = input("Make a word or letter guess: ")
        if userGuess == word:
            print("You win.")
            break
        elif userGuess in word:
            guessList.append(userGuess)
        else:
            guessList.append(userGuess)
            state += 1

    print(pictures[state])
    print("You lose. The word was %s" %word)

hangMan()


