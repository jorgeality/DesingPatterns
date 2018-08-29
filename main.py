from Patterns.abstractFactory import convertionFactory
from pypattyrn.structural.adapter import Adapter
from convertionSystem.toCentimeters import toCentimeters
from convertionSystem.toDollar import toDollar
from convertionSystem.toPesos import toPesos
from convertionSystem.toMeters import toMeters


systemConvertion = convertionFactory()

while True:

    option = int(input(
        'what do you want to do: \n units of longitude \n\t 1. Convert centimeters to Meters . \n\t 2. Convert  Meters to Centimeters.'
        '\n currency\n\t 3. convert dollar to pesos. \n\t 4. convert pesos to dollar. \n 5. Exit \n select your option: '))
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
    elif option == 3:
        number = float(input(' number of dollars : '))
        toPesos = systemConvertion.create(option, number)
        result_adapter = Adapter(toPesos, result=toPesos.convert)
        """
            in this part I applied singleton pattern to create always the same instance of  toPesos object        
        """
        # print(toPesos) if you want to look that is the same instance uncomment this line

    elif option == 4:
        number = float(input(' number of pesos : '))
        toDollar = systemConvertion.create(option, number)
        result_adapter = Adapter(toDollar, result=toDollar.convert)
        """
            in this part I applied singleton pattern to create always the same instance of  toDollar object        
        """
        # print(toDollar) if you want to look that is the same instance uncomment this line

    else:
        break

    print('Final Result : ', result_adapter.result())
    print('******************************************')
