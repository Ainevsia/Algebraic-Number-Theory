def fast_power(b, n, m):
    """
    Use the Fast-Power Algorithm to calculate the result of (b^n mod m).

    :param b: integer, base nubmer.
    :param n: integer, exponent number.
    :param m: integer, the modulus.
    :return: integer, the result of (b^n mod m).
    """
    a = 1
    while n:  # n is represented as a 2's complement number
        if n & 1:  # test the lowest bit of n
            a = (a * b) % m
        b = (b * b) % m
        n //= 2  # right shift 1 bit
    return a