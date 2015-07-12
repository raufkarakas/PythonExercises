__author__ = 'rkarakas'

userInput = int(input("Enter the number to see the steps: "))

def collatzConjecture(n):
    if n % 2 == 0:
        n /= 2
        print(n)
        collatzConjecture(n)
    elif n % 2 == 1:
        if n != 1:
            n = 3 * n + 1
            print(n)
            collatzConjecture(n)
        else:
            print("Process completed.")
    else:
        print("Invalid value entered.")

collatzConjecture(userInput)
