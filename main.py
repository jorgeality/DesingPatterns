from Patterns.factory import convertionFactory
from convertionSystem.toCentimeters import toCentimeters
from convertionSystem.toMeters import toMeters




systemConvertion = convertionFactory()

while True:
    print('******************************************')
    option = int(input(
        'what do you want to do: \n 1. Convert centimeters to Meters . \n 2. Convert  Meters to Centimeters. \n 3. Exit \n select your option: '))
    if option == 1:

        number = float(input(' number of centimeters : '))
        toMeters = systemConvertion.create(option, number)
        toMeters.convert()
        print(toMeters)
    elif option == 2:

        number = float(input(' number of meters : '))
        toCentimeters = systemConvertion.create(option, number)
        toCentimeters.convert()
        print(toCentimeters)
    else:
        break

    print('******************************************')
