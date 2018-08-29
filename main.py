from Patterns.factory import convertionFactory
from pypattyrn.structural.adapter import Adapter#implementing adapter pattern
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
        result_adapter = Adapter(toMeters, result=toMeters.convert)
        """
            in this part I applied singleton pattern to create always the same instance of  toMeters object        
        """
        #print(toMeters) if you want to look that is the same instance uncomment this line
    elif option == 2:

        number = float(input(' number of meters : '))
        toCentimeters = systemConvertion.create(option, number)
        result_adapter = Adapter(toCentimeters, result=toCentimeters.convert)
        """
            in this part I applied singleton pattern to create always the same instance of  toCentimeters object        
        """
        #print(toCentimeters) if you want to look that is the same instance uncomment this line
    else:
        break

    print('Final Result : ', result_adapter.result())
    print('******************************************')
