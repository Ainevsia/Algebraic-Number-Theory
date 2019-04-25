from RandBigPrime import random_prime
from fast_power import fast_power
from str_rsa import *

byte = 128  # nubmer of bytes of p and q
p = random_prime(byte)  # p,q is byte * 8 bit big integers
q = random_prime(byte)
n = p * q
phi = (p - 1) * (q - 1),
e = random_prime(2)  # (e,n) are the public key
while phi % e == 0:  # generate e st. (e,phi(n)) = 1
    e = random_prime(2)

# in case the message to be encrypted is too long
max_len = (len(hex(n).replace('0x', ''))) // 2

# preparations
d = inverse(phi, e) % phi  # (d,n) are the private key
a = input('message to encrypt: ')
if len(a) > max_len:
    a = a[0:max_len - 1]

# encrypting
ciphertext = fast_power(eval(hexify(a)), e, n)
print('message encrypted: ' + str(ciphertext))

# decrypting
plaintext = hex(fast_power(ciphertext, d, n)).replace('0x', '')
print('decrypted message: ' + stringify(plaintext))
