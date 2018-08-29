#implementing singleton design pattern


from pypattyrn.creational.singleton import Singleton


#class implemented to convert meters to centimeters
"""
    this class is implemented with singleton pattern
    to create always the same instance of this
"""
class toDPesos(object, metaclass=Singleton):

    dollar = 0
    #constructor
    def __init__(self, value):
        self.dollar = value

    # method responsible for converting meters to centimeters
    """
        the value returned by this method is used to implement adapter pattern in the main class
    """
    def convert(self):
        pesos = self.dollar * 3000
        return str(self.dollar) +' pesos is/are ' +str(pesos) +' Dollars'
