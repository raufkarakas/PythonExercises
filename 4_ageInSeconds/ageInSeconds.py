__author__ = 'rkarakas'

from datetime import *

def ageInSeconds():
    birth = input("Please enter your birth date (DD.MM.YYYY) -> ")
    age = datetime.now() - datetime.strptime(birth, "%d.%m.%Y")
    print("You have been living %i seconds." %(age.total_seconds()))

ageInSeconds()