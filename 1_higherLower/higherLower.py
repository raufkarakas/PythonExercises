__author__ = 'rkarakas'

import random

def higherLower():
    print("So you want to guess what is the chosen number between 0 and 100?")
    chosenNumber = random.randint(0,100)
    guess = 101
    predictNumber = 0

    while guess != chosenNumber:
        guess = int(input("What is your guess? -> "))
        predictNumber += 1
        if guess < chosenNumber:
            print("Higher than you think.")
        elif guess > chosenNumber:
            print("Lower than you think.")

    print("You found it after %i try! Yaayyy!" %(predictNumber))

higherLower()