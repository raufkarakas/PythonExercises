__author__ = 'rkarakas'

def loveCalculator():
    name1 = input("Your name: ")
    name2 = input("Your crush's name: ")

    score = len(name1) + len(name2)
    if len(name1) > len(name2):
        score -= 5
    else:
        score += 3

    score *= 42
    score = score / (100 + len(name2))

    if score > 10:
        score = 10
    else:
        round(score, 0)

    print("%s and %s has a love score %i out of 10" %(name1, name2, score))

loveCalculator()