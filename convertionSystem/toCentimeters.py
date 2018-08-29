#implementing singleton design pattern


from pypattyrn.creational.singleton import Singleton


#class implemented to convert meters to centimeters
"""
    this class is implemented with singleton pattern
    to create always the same instance of this
"""
class toCentimeters(object, metaclass=Singleton):

    meters = 0
    #constructor
    def __init__(self, value):
        self.meters = value

    # method responsible for converting meters to centimeters
    """
        the value returned by this method is used to implement adapter pattern in the main class
    """
    def convert(self):
        centimeters = self.meters * 100
        return str(self.meters) +' meters is/are ' +str(centimeters) +' centimeters'
