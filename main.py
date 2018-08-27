from Patterns.factory import convertionFactory
from convertionSystem.toCentimeters import toCentimeters
from convertionSystem.toMeters import toMeters



option = int(input('what do you want to do: \n 1. Convert centimeters to Meters . \n 2. Convert  Meters to Centimeters \n select your option: '))



if option == 1:
    systemConvertion = convertionFactory()
    number = float(input('number of centimeters : '))
    toMeters = systemConvertion.create(option, number)
    toMeters.convert()
elif option == 2:
    systemConvertion = convertionFactory()
    number = float(input('number of meters : '))
    toCentimeters = systemConvertion.create(option, number)
    toCentimeters.convert()

