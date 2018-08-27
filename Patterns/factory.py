from convertionSystem.toCentimeters import toCentimeters
from convertionSystem.toMeters import toMeters

from pypattyrn.creational.factory import Factory  # This is just an interface

class convertionFactory(Factory):  # A factory class for creating animals.

    def create(self, convertion_type, number):  # Implement the abstract create method.
        if convertion_type == 1:

            return toMeters(number)

        elif convertion_type == 2:

            return toCentimeters(number)

        else:
            return None