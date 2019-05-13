from toolkit import *


def ord_power_d(m, a, d):
    small_ord = ord(m, a)
    return small_ord // gcd(small_ord, d)


if __name__ == '__main__':
    m, a, b = pow(2, 8), 5, 11
    print('ord_m(a)  =', ord(m, a))
    print('ord_m(b)  =', ord(m, b))
    print('ord_m(ab) =', ord(m, a * b))
