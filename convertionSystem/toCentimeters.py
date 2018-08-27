#class implemented to convert meters to centimeters
class toCentimeters(object):

    meters = 0
    #constructor
    def __init__(self, value):
        self.meters = value

    # method responsible for converting meters to centimeters
    def convert(self):
        centimeters = self.meters * 100
        print(self.meters,'meters is/are ', centimeters,'centimeters')
