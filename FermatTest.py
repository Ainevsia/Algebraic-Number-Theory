from Prime import prime


def fermat_test(p, n):
    """
    Use the Fermat law to test whether a randomly generated big integer
    is a prime number or not.

    :param p: integer to be tested.
    :param n: integer, to test the first n values of 'a'.
    :return: bool, is prime or not.
    """
    for i in range(n):
        a = prime[i]
        if pow(a, p - 1, p) != 1:
            return False
    return True
