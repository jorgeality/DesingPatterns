
#class implemented to convert centimeters to meters

class toMeters(object):

    centimeters = 0

    def __init__(self, value):
        self.centimeters = value

    def convert(self):

        meters =  self.centimeters / 100

        print(self.centimeters,' centimeters is/are ', meters,' meters')
