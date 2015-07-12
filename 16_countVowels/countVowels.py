__author__ = 'rkarakas'

userPrompt = input("Enter the text to know how many vowel it has: ")

def countVowels(userInput):
    vowelList = ["a", "e", "i", "o", "u"]
    vowelCount = 0
    for char in userInput:
        if char in vowelList:
            vowelCount += 1
    print("Text '%s' has %i vowel(s) in it." %(userPrompt, vowelCount))

countVowels(userPrompt)
