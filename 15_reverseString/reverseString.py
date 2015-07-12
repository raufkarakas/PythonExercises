__author__ = 'rkarakas'

userInput = input("Enter the string that will be reversed: ")

def reverseString(text):
    reversed = ""
    for i in range(len(text)):
        reversed += text[len(text) - 1 - i]
    print(reversed)

reverseString(userInput)
