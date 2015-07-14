__author__ = 'rkarakas'

def bmiCalculator(height, weight):
    heightInMeter = height / 100
    return weight / (heightInMeter ** 2)

userHeight = int(input("Enter your height in cm: "))
userWeight = int(input("Enter your weight in kg: "))

print("Your BMI value is %2d" %bmiCalculator(userHeight, userWeight))