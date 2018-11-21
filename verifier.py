from utils import *

class Verifier:
    """
    checks if the received message is correct
    """

    def __init__(self, data, divisor):
        """
        Instances Attributes:
        ---------------------
                    'self.__message': holds the string of 0s and 1s of the message to be encoded
                    'self.__divisor': holds the string of 0s and 1s of the polynomial
        """
        self.__data = data
        self.__divisor = divisor

    def verify(self):
        """
        prints 'message is correct' if the received message is correct, otherwise it prints 'message is not correct'
        """
        # divisorLength = len(self.__divisor)
        # # Appends n-1 zeroes at end of data
        # appended_data = self.__data + '0'*(divisorLength - 1)

        remainder = mod2div(self.__data, self.__divisor)

        # If remainder is all zeros then no error occured
        temp = "0" * (len(self.__divisor) - 1)
        if remainder == temp:
            print('message is correct')
        else:
            print('message is not correct')
