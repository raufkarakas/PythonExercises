__author__ = 'rkarakas'

from random import choice

def haikuGenerator():
    haikuLine = []
    lines = open("mhyph.txt").readlines()
    remainingSyllabus = [5, 7, 5]
    for value in remainingSyllabus:
        tempLine = ""
        while value > 0:
            syllabus = 1
            word = choice(lines)[:-1]
            for char in word:
                if char == "*" or char == "-":
                    syllabus += 1
            if (value - syllabus >= 0):
                tempLine += word + " "
                value -= syllabus
        haikuLine.append(tempLine)

    print(haikuLine[0].replace("*", "") + "\n" + haikuLine[1].replace("*", "") + "\n" + haikuLine[2].replace("*", ""))

haikuGenerator()