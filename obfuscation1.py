# this .py program solves the equation like x^n mod m = right value
# where m is not prime and m = p1 * p2 * p3
from toolkit import *
import binascii

nlst = [0x3409E4A9, 0x38732A5B, 0x3DFEBE85, 0x2E89A11D]
mlst = [0xD12BE249, 0xAE3EBFCF, 0xBA0D25B9, 0xBE70D1B1]
rightlst = [0xCCFBA11F, 0x7CCDC7C1, 0x2DBDFBCE, 0x1C9CEE8C]
# m = 0xD12BE249
# n = 0x3409E4A9
# right = 0xCCFBA11F
for i in range(4):
    m = mlst[i]
    n = nlst[i]
    right = rightlst[i]
    plst = factor(m)
    M = [plst[1] * plst[2], plst[0] * plst[2], plst[0] * plst[1]]
    M = [M[0] * (inverse_a_mod_p(M[0], plst[0]) % plst[0]),
         M[1] * (inverse_a_mod_p(M[1], plst[1]) % plst[1]),
         M[2] * (inverse_a_mod_p(M[2], plst[2]) % plst[2])]
    x = 0
    for j in range(3):
        n_eqv = n % phi(plst[j])
        for b in range(1, plst[j]):
            if pow(b, n_eqv, plst[j]) == right % plst[j]:
                x += b * M[j]
                break
    print(pow(x, n, m) - right)
    x %= m
    print("{:x}".format(x))
    # print(pow(x, n, m) - right)
string = '61336132356134373238333537383939'
print(binascii.unhexlify(string))
'2a3a74a553829987'
