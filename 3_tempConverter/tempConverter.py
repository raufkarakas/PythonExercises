__author__ = 'rkarakas'

def tempConverter():
    print("Please choose conversion method:")
    print("1- Celsius to Fahrenheit")
    print("2- Fahrenheit to Celsius")
    selection = float(input("Please select (1/2) -> "))
    tempValue = float(input("Enter the temperature value. -> "))

    if selection == 1:
        print("%.2f Celsius equals %.2f Fahrenheit" %(tempValue, (tempValue * 1.8) + 32))
    elif selection == 2:
        print("%.2f Fahrenheit equals %.2f Celsius" %(tempValue, (tempValue - 32) / 1.8))
    else:
        print("Please enter 1 or 2")
        tempConverter()


tempConverter()