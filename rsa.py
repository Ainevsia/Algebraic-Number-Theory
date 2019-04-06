from RandBigPrime import random_prime
from fast_power import fast_power
from str_rsa import *

byte = 128
p = random_prime(byte)
q = random_prime(byte)
n = p * q
max_len = (len(hex(n).replace('0x', ''))) // 2
phi = (p - 1) * (q - 1)
e = 65537

d = inverse(phi, e) % phi
a = input('message 2 encrypt: ')
if len(a) > max_len:
    a = a[0:max_len - 1]

c = fast_power(eval(hexify(a)), e, n)
print('message encrypted: ' + stringify(str(c)))

plaintext = hex(fast_power(c, d, n)).replace('0x', '')
if len(plaintext) % 2 == 1:
    plaintext = '0' + plaintext
print('decrypted message: ' + stringify(plaintext))
