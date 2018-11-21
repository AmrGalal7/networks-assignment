from utils import *

class Generator:
    """
    encodes a message based on a given polynomial/ divisor

    Class Attribute:
    ----------------
                    'GeneratorDivider': stores the polynomial, so it can be sent to the Verifier Class
    """

    GeneratorDivisor = None

    def __init__(self, message, divisor):
        """
        Instances Attributes:
        ---------------------
                    'self.__message': holds the string of 0s and 1s of the message to be encoded
                    'self.__divisor': holds the string of 0s and 1s of the polynomial
        """
        self.__message = message
        self.__divisor = divisor

    def getDivisor(self):
        """
        Return:
        -------
                    the string representation of the polynomial
        """
        return self.__divisor


    def encode(self):
        """
        Return:
        -------
                    a string representation of the encoded message
        """

        divisorLength = len(self.__divisor)
        # Appends n-1 zeroes at end of message
        appended_data = self.__message + '0'*(divisorLength - 1)

        # apply CRC:

        remainder = mod2div(appended_data, self.__divisor)
        # Append the remainder to the original message
        codeword = self.__message + remainder

        # save the message on disk
        with open('transmitted_msg.txt', 'w') as f:
            f.write(codeword)

        return codeword
