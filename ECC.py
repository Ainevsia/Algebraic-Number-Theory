p = 17
a4, a6 = 3, 1
E = (a4, a6, p)

def inverse(a, p):
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
    elif P[0] == Q[0] and P[1] + Q[1] == 0: return 'O'
    else:
        x1, y1, x2, y2 = P[0], P[1], Q[0], Q[1]
        (a4, a6, p) = E
        if x1 == x2:
            lambda_ecc = ((3 * pow(x1, 2) + a4) * inverse(2 * y1, p)) % p
        else:
            print('y2 - y1 =', (y2 - y1))
            print('inverse =', inverse(x2 - x1, p))
            lambda_ecc = ((y2 - y1) * inverse(-x2 - x1, p)) % p
        print('lamda', lambda_ecc)
        x3 = (pow(lambda_ecc, 2) - x1 - x2) % p
        y3 = (lambda_ecc * (x1 - x3) - y1) % p
        return (x3, y3)


def test():
    # print(add(E, (1,2), negate((1,2))))
    print(add(E,  (2,7),(0,16)))
    print('<<<<<<<<false\n>>>>>>>>true')
    print(add(E,  (0,16),(2,7)))
    # P_k = add(E, (2,7), (2,7))
    # for i in range(14):
    #     print("{:2}P {}".format(i + 2, P_k))
    #     P_k = add(E, (2,7), P_k)


if __name__ == "__main__":
    test()