#implementing singleton design pattern
from pypattyrn.creational.singleton import Singleton

#class implemented to convert centimeters to meters
"""
    this class is implemented with singleton pattern
    to create always the same instance of this
"""
class toMeters(object, metaclass=Singleton):

    centimeters = 0

    # constructor
    def __init__(self, value):
        self.centimeters = value

    # method responsible for converting centimeters to meters
    """
        the value returned by this method is used to implement adapter pattern in the main class
    """
    def convert(self):
        meters =  self.centimeters / 100
        return str(self.centimeters)+' centimeters is/are '+str(meters)+' meters'
