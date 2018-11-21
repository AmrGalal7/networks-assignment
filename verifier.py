class Verifier:
    """
    checks if the received message is correct
    """

    def __init__(self, data, divider):
        """
        Instances Attributes:
        ---------------------
                    'self.__message': holds the string of 0s and 1s of the message to be encoded
                    'self.__divider': holds the string of 0s and 1s of the polynomial
        """
        self.__data = data
        self.__divider = divider

    def verify(self):
        """
        prints 'message is correct' if the received message is correct, otherwise it prints 'message is not correct'
        """
        dataDecimal = int(self.__data, 2)
        dividerDecimal = int(self.__divider, 2)

        # if the message is divisible by the polynomial, then it's correct
        if dataDecimal % dividerDecimal == 0:
            print('message is correct')
        else:
            print('message is not correct')
