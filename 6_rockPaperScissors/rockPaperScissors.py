__author__ = 'rkarakas'

import random

def rockPaperScissors():
    userInput = input("Rock, Paper or Scissors? (R/P/S) -> ")
    possibleMoves = [["s", "r"], ["s", "p"], ["s", "s"],
                       ["r", "p"], ["r", "s"], ["r", "r"],
                       ["p", "s"], ["p", "r"], ["p", "p"]]
    move = [userInput.lower(), random.choice(["r","p","s"])]
    if move not in possibleMoves:
        print("Not a valid move.")
        rockPaperScissors()
    elif possibleMoves.index(move)%3 == 0:
        print("You lose. Computer selected: %s" %move[1])
    elif possibleMoves.index(move)%3 == 1:
        print("You win. Computer selected: %s" %move[1])
    else:
        print("Tie game. Computer also selected: %s" %move[1])


rockPaperScissors()