__author__ = 'rkarakas'

def fizzBuzz(loopValue):
    for i in range(loopValue):
        if i%3 == 0 and i%5 == 0:
            print("fizz buzz")
        elif i%3 == 0:
            print("fizz")
        elif i%5 == 0:
            print("buzz")
        else:
            print(i)

fizzBuzz(50)
