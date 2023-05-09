"""
COMP.CS.100 
Comparing floating-point (decimal) numbers
"""
def main():

    """
    values for compare floats function
    :return: boolean
    """

    float_1 = float(input("First float: "))
    float_2 = float(input("Second float: "))
    ep = float(input("Epsilon: "))

    print(compare_floats(float_1, float_2, ep))

def compare_floats(float_1, float_2, ep):
    """
    This function cmopares floats
    :param float_1:
    :param float_2:
    :param EPSILON:
    :return: boolean
    """

    if abs(float_1 - float_2) < ep:
        return True

    else:
        return False

if __name__ == "__main__":
    main()