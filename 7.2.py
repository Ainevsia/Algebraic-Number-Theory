from fractions import Fraction
from toolkit import *


def bezout(a, b):
    """
    :return s and t st. sa + tb = (a,b)
    """
    s, t, sn, tn, r = 1, 0, 0, 1, 1
    while r != 0:
        q, r = divmod(a, b)
        st, tt = sn * (-q) + s, tn * (-q) + t
        s, t = sn, tn
        sn, tn = st, tt
        a, b = b, r
    return s, t


def bezout_unittest():
    x, y = 1859, 1573
    s, t = bezout(x, y)
    if s * x + t * y == gcd(x, y):
        print('yes')
    x, y = 7700, 2145
    s, t = bezout(x, y)
    if s * x + t * y == gcd(x, y):
        print('yes')


def continued_fraction_bezout(x, y):
    n = Fraction(x, y)
    P_nm2, P_nm1, Q_nm2, Q_nm1, P_n, Q_n = 0, 1, 1, 0, 0, 0
    for i in range(10):
        a = int(n)
        P_n, Q_n = a * P_nm1 + P_nm2, a * Q_nm1 + Q_nm2
        P_nm2, P_nm1, Q_nm2, Q_nm1 = P_nm1, P_n, Q_nm1, Q_n
        x = n - a
        if x != 0:
            n = 1 / x
        else:
            s = Q_nm2 * (1 if i & 1 == 1 else -1)
            t = P_nm2 * (1 if i & 1 == 0 else -1)
            return s, t

for i in range(10):
    x, y = randint(1), randint(1)
    # print(x, y)
    if continued_fraction_bezout(x, y) == bezout(x, y):
        print('yes')
