__author__ = 'Zhipeng Xu'
__modified__ = '2019-12-20 20:12:28'


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

def hk14_2_4_1():
    print("homework eg 14.2.4 question (1)")
    p = 17
    a4, a6 = 2, 3
    E = (a4, a6, p) # Elliptic Curves

    P = 'O'
    P1 = (5,6)
    cnt = 0

    while P != 'O' or cnt == 0:
        cnt += 1
        P = add(E, P, P1)
        print('{:2}P {}'.format(cnt, P))

    print("#(E) = {}".format(cnt))

def hk14_2_4_2():
    print("homework eg 14.2.4 question (2)")
    p = 17
    a4, a6 = 2, 3
    E = (a4, a6, p) # Elliptic Curves

    P = 'O'
    P1 = (9,6)
    cnt = 0

    while P != 'O' or cnt == 0:
        cnt += 1
        P = add(E, P, P1)
        print('{:2}P = {}'.format(cnt, P))

    print("#(E) = {}".format(cnt))

def hk14_2_6():
    print("homework eg 14.2.6")
    p = 17
    a4, a6 = 3, 1
    E = (a4, a6, p) # Elliptic Curves

    P = 'O'
    P1 = (2,7)
    cnt = 0
    lst = []

    while P != 'O' or cnt == 0:
        cnt += 1
        P = add(E, P, P1)
        print('{:2}P = {}'.format(cnt, P))
        lst.append(P)

    print("#(E) = {}".format(cnt))
    return lst

def plt_hk14_2_6(lst):
    print(lst.pop()) # remove the inf point
    import matplotlib.pyplot as plt

    (x, y) = (list(tup) for tup in list(zip(*lst)))
    plt.scatter(x, y, s=250)
    i = 0
    for (xi, yi) in zip(x, y):
        i += 1
        if i == len(x):
            plt.annotate('{}P'.format(i), (xi-1, yi-1))
            break
        plt.arrow(xi, yi, x[i] - xi, y[i] - yi,
            width=0.05, shape='full', head_width=0.5, head_length=0.75,
            length_includes_head=True, facecolor='black',)
        plt.annotate('{}P'.format(i), (xi-1, yi-1))
    plt.xlim(-1, 16)
    plt.ylim(-1, 17)
    plt.show()


if __name__ == "__main__":
    # hk14_2_4_1()
    # hk14_2_4_2()
    plt_hk14_2_6(hk14_2_6())