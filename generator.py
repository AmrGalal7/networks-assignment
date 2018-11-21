class Generator:

    GeneratorDivider = None

    def __init__(self, message, divider):
        self.message = message
        self.__divider = divider

    def getDivider(self):
        return self.__divider

    def encode(self):
        messageDecimal = int(self.message, 2)
        dividerDecimal = int(self.__divider, 2)

        remainder = messageDecimal - (messageDecimal // dividerDecimal ) * dividerDecimal

        data = str(bin(messageDecimal * 2**len(self.__divider) - remainder))[2:]
        with open('transmitted_msg.txt', 'w') as f:
            f.write(data)

        return data
