__author__ = 'rkarakas'

import random
import string

def passwordGenerator(length, method):
    password = ""
    characterPool = string.ascii_letters
    if method == 1:
        characterPool += string.digits
    elif method == 2:
        characterPool += string.digits
        characterPool += string.punctuation
    else:
        print("Invalid option. Considered as option 0")

    for i in range(length):
        password += characterPool[random.randint(0, len(characterPool))]

    return password

print("Method 0: Uppercase and lowercase letters.")
print("Method 1: Uppercase & lowercase letters and digits.")
print("Method 2: Uppercase & lowercase letters, digits, and punctuations.")
print(passwordGenerator(int(input("Length of the password? -> ")), int(input("Method? ->"))))


