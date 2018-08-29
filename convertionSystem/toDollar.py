#implementing singleton design pattern
from pypattyrn.creational.singleton import Singleton


#class implemented to convert meters to centimeters
"""
    this class is implemented with singleton pattern
    to create always the same instance of this
"""
class toDollar(object, metaclass=Singleton):

    pesos = 0
    #constructor
    def __init__(self, value):
        self.pesos = value

    # method responsible for converting meters to centimeters
    """
        the value returned by this method is used to implement adapter pattern in the main class
    """
    def convert(self):
        dollars = self.pesos / 3000
        return str(self.pesos) +' pesos is/are ' +str(dollars) +' Dollars'
