
def xor(a, b):
    """
    Parameters:
    ----------
                a: first operand
                b: second operand
    Return:
    -------
                the xor result between a and b
    """

    # initialize result
    result = []

    # Traverse all bits, if bits are
    # same, then XOR is 0, else 1
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')

    return ''.join(result)


def mod2div(divident, divisor):
    """
    Parameters:
    -----------
                divident: a slice of the appended message of the same length as 'divisor'
                divisor: the polynomial
    Return:
    -------
                The modulo 2 division between slice of a message and the polynomial

    """

    # Number of bits to be XORed at a time.
    pick = len(divisor)

    # Slicing the divident to appropriate length for particular step
    tmp = divident[0 : pick]

    while pick < len(divident):

        if tmp[0] == '1':

            # replace the divident by the result of XOR and pull 1 bit down
            tmp = xor(divisor, tmp) + divident[pick]
        else:
            # If leftmost bit is '0':
            tmp = xor('0'*pick, tmp) + divident[pick]

        # increment pick to move further
        pick += 1

    # For the last n bits, we have to carry it out normally as increased value of pick will cause Index Out of Bounds.
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)

    checkword = tmp

    return checkword
