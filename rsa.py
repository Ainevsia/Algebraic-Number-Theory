from RandBigPrime import random_prime
from fast_power import fast_power

p = random_prime(10)
q = random_prime(10)
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
