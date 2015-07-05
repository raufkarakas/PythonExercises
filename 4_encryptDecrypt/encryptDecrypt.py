__author__ = 'rkarakas'

def encrypt(text, value):
    encryptedText = ""
    for char in text:
        encryptedText += chr(ord(char) + value)
    return encryptedText

def decrypt(text, value):
    decryptedText = ""
    for char in text:
        decryptedText += chr(ord(char) - value)
    return decryptedText

methodInput = input("Please select method (E/D): ")
valueInput = int(input("Please enter value: "))
textInput = input("Enter the text: ")

if methodInput.lower() == "e":
    print(encrypt(textInput, valueInput))
elif methodInput.lower() == "d":
    print(decrypt(textInput, valueInput))
else:
    print("Invalid option.")

