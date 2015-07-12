__author__ = 'rkarakas'

userPromt = input("Enter the text to know how many words it has: ")

def countWords(userInput):
    userInput = " ".join(userInput.split())
    wordsCounted = 1
    for char in userInput:
        if char == " ":
            wordsCounted += 1
    print("Text you entered has %i word(s) in it." %wordsCounted)

countWords(userPromt)