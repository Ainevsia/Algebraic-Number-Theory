def inverse(a, p):
    a = a % p # make sure a and p are both positive
    s, t, sn, tn, r = 1, 0, 0, 1, 1
    while r != 0:
        q = p // a
        r = p - q * a
        st, tt = sn * (-q) + s, tn * (-q) + t
        s, t = sn, tn
        sn, tn = st, tt
        p = a
        a = r
    return t

def negate(P):
    if P == 'O': return 'O'
    else:
        return(P[0], -P[1])

def add(E, P, Q):
    if P == 'O':    return Q
    elif Q == 'O':  return P
    elif P[0] == Q[0] and (P[1] + Q[1]) % E[2] == 0: return 'O'
    else:
        x1, y1, x2, y2 = P[0], P[1], Q[0], Q[1]
        (a4, a6, p) = E
        if x1 == x2:
            lambda_ecc = (3 * pow(x1, 2) + a4) * inverse(2 * y1, p)
        else:
            lambda_ecc = (y2 - y1) * inverse(x2 - x1, p)
        x3 = (pow(lambda_ecc, 2) - x1 - x2) % p
        y3 = (lambda_ecc * (x1 - x3) - y1) % p
        return (x3, y3)


def eg14_2_6():
    p = 17
    a4, a6 = 3, 1
    E = (a4, a6, p) # Elliptic Curves

    P_k = add(E, (2,7), (2,7))
    for i in range(15):
        print("{:2}P {}".format(i + 2, P_k))
        P_k = add(E, (2,7), P_k)

def eg14_2_4():
    p = 17
    a4, a6 = 2, 3
    E = (a4, a6, p) # Elliptic Curves

    print("P+Q =", add(E, (2,7), (11,8)))
    P = (2, 7)
    P2 = add(E, P, P)
    print(" 2P =", P2)
    P4 = add(E, P2, P2)
    print(" 4P =", P4)
    P8 = add(E, P4, P4)
    print(" 8P =", P8)
    P10 = add(E, P2, P8)
    print("10P =", P10)
    P11 = add(E, P, P10)
    print("11P =", P11)
    P22 = add(E, P11, P11)
    print("11P =", P22)

if __name__ == "__main__":
    eg14_2_4()