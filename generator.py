class Generator:
    """
    encodes a message based on a given polynomial/ divider

    Class Attribute:
    ----------------
                    'GeneratorDivider': stores the polynomial, so it can be sent to the Verifier Class
    """

    GeneratorDivider = None

    def __init__(self, message, divider):
        """
        Instances Attributes:
        ---------------------
                    'self.__message': holds the string of 0s and 1s of the message to be encoded
                    'self.__divider': holds the string of 0s and 1s of the polynomial
        """
        self.__message = message
        self.__divider = divider

    def getDivider(self):
        """
        Return:
        -------
                    the string representation of the polynomial
        """
        return self.__divider

    def encode(self):
        """
        Return:
        -------
                    a string representation of the encoded message
        """

        # convert the string value of a binary number to int
        messageDecimal = int(self.__message, 2)
        dividerDecimal = int(self.__divider, 2)

        # calculate the remainder of the division of the message by the polynomial
        remainder = messageDecimal - (messageDecimal // dividerDecimal ) * dividerDecimal

        # shift the binary message to the right x digits, where x is the degree of the polynomial, then subtract the remainder from it.
        # shifting (for decimals): multiplication by 2 raised to some power
        # degree of the polynomial: length of the polynomial
        # the message becomes in the format: 0b10110
        # the indexing to skip '0b'
        # the message is then converted into string
        data = str(bin(messageDecimal * 2**len(self.__divider) - remainder))[2:]

        # save the message on disk
        with open('transmitted_msg.txt', 'w') as f:
            f.write(data)

        return data
