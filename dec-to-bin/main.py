def recDecimalToBinary(decimal_in, remainders):

    if decimal_in == 0:
        return remainders

    remainders =  str(decimal_in % 2) + remainders
    return str(recDecimalToBinary(int(decimal_in/2),remainders))

def decimalToBinary(decimal_in):
    """
    :param decimal_in: int decimal number to convert to binary
    :return: string binary representation of the decimal
    """
    remainders = ""
    return recDecimalToBinary(decimal_in, remainders)


def test_decimalToBinary_3():
    assert decimalToBinary(3) == "11"

def test_decimalToBinary_8():
    assert decimalToBinary(8) == "1000"

                         
def test_decimalToBinary_803131524():
    assert decimalToBinary(803131524) == "101111110111101101000010000100"
