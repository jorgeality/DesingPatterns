class toCentimeters(object):

    meters = 0

    def __init__(self, value):
        self.meters = value

    def convert(self):
        centimeters = self.meters * 100

        print(self.meters,'meters is/are ', centimeters,'centimeters')
