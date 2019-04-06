from random import Random
from Prime import prime
from FermatTest import fermat_test


def random_str(randomlength):
    """
    Generate a qualified Hex number, containing character from 0 to f.

    :param randomlength: integer, lengeth of the string.
    :return: a string.
    """
    ret_str = ''
    chars = 'abcdef0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        ret_str += chars[random.randint(0, length)]
    return ret_str


def random_prime(byte):
    """
    Use a randomly generated hex string, fermat test to generate a
    pseudo-prime number.

    :param bit: integer, number of bytes of the prime number (usually 128).
    :return: integer, a pseudo-prime number
    """
    while True:
        ran_int = eval('0x' + random_str(2 * byte))
        if ran_int & 1 == False:
            ran_int += 1
        notprime = False
        for i in range(len(prime)):
            if ran_int % prime[i] == 0:
                notprime = True
                break
        if notprime:
            pass
        elif fermat_test(ran_int, 16) == False:
            pass
        else:
            return ran_int
