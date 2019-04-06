from RandBigPrime import random_prime

p = random_prime()
q = random_prime()
n = p * q
phi = (p - 1) * (q - 1)
e = 65537


def cald(phi, e):
    s, t, sn, tn, r = 1, 0, 0, 1, 1
    while r != 0:
        q = phi // e
        r = phi - q * e
        st, tt = sn * (-q) + s, tn * (-q) + t
        s, t = sn, tn
        sn, tn = st, tt
        phi = e
        e = r
    return t


def fast_power(b, n, m):
    """
    Use the Fast-Power Algorithm to calculate the result of (b^n mod m).

    :param b: integer, base nubmer.
    :param n: integer, exponent number.
    :param m: integer, the modulus.
    :return: integer, the result of (b^n mod m)
    """
    a = 1
    while n:  # n is represented as a 2's complement number
        if n & 1:  # test the lowest bit of n
            a = (a * b) % m
        b = (b * b) % m
        n //= 2  # right shift 1 bit
    return a


# used to convert message to hex integers
def hexify(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        lst.append(hv)
    return '0x' + ''.join(lst)


d = cald(phi, e) % phi
a = input('please input the message you want to encrypt:')
c = fast_power(eval(hexify(a)), e, n)
print(c)
plaintext = hex(fast_power(c, d, n)).replace('0x', '')
if len(plaintext) % 2 == 1:
    plaintext = '0' + plaintext


def stringify(plaintext):
    lst = []
    end = len(plaintext) // 2
    for i in range(end):
        lst.append(chr(eval('0x' + plaintext[2 * i: 2 * (i + 1)])))
    return ''.join(lst)


print(stringify(plaintext))
