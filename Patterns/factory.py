#importing necessary classes to implement factory design pattern
from convertionSystem.toCentimeters import toCentimeters
from convertionSystem.toMeters import toMeters
from pypattyrn.creational.factory import Factory  # This is just an interface


#class responsible for implementing the factory design pattern
class convertionFactoryLongitude(Factory):  # A factory class for creating animals.

    #method responsible for units conversión
    #@param convertion_type is the option selected to convert from one unit to another.
    #@param number is the units amount to convert
    #@return a class, contains the desired value in the necessary unit
    def create(self, convertion_type, number):  # Implement the abstract create method.
        if convertion_type == 1:
            return toMeters(number)
        elif convertion_type == 2:
            return toCentimeters(number)
        else:
            return None

#class responsible for implementing the factory design pattern
class convertionFactoryCurrency(Factory):  # A factory class for creating animals.

    #method responsible for units conversión
    #@param convertion_type is the option selected to convert from one unit to another.
    #@param number is the units amount to convert
    #@return a class, contains the desired value in the necessary unit
    def create(self, convertion_type, number):  # Implement the abstract create method.
        if convertion_type == 3:
            return toMeters(number)
        elif convertion_type == 4:
            return toCentimeters(number)
        else:
            return None