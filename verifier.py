class Verifier:

    def __init__(self, data, divider):
        self.data = data
        self.divider = divider

    def verify(self):
        dataDecimal = int(self.data, 2)
        dividerDecimal = int(self.divider, 2)

        if dataDecimal % dividerDecimal == 0:
            print('message is correct')
        else:
            print('message is not correct')
