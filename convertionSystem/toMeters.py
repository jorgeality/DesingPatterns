#implementing singleton design pattern
from pypattyrn.creational.singleton import Singleton

#class implemented to convert centimeters to meters
class toMeters(object, metaclass=Singleton):

    centimeters = 0

    # constructor
    def __init__(self, value):
        self.centimeters = value

    # method responsible for converting centimeters to meters
    def convert(self):
        meters =  self.centimeters / 100
        return str(self.centimeters)+' centimeters is/are '+str(meters)+' meters'
