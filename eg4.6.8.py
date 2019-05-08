from toolkit import *


def solve_x_for_x2_equiv_a_mod_p(a, p):
    # if p not in prime:
    #     print("p is not a prime number")
    #     return 0

    # factor p-1
    t, s = 0, p - 1
    while s & 1 == 0:  # while s is still an even number
        t += 1
        s, unused = divmod((p - 1), pow(2, t))
    print('p - 1 =', p - 1, '= 2 ^', t, '*', s)
    print('so, t =', t, 'and s =', s)
    t -= 2
    base = t

    # choose n
    n = 0
    for i in range(2, p):
        if Legendre(i, p) == -1:
            n = i
            break
    b = pow(n, s, p)
    x = pow(a, (s + 1) // 2, p)
    inv_a = inverse_a_mod_p(a, p) % p
    print('choose n =', n, 'and let b = n^s (mod p) =', b)
    print('a^-1 =', inv_a)

    # loop
    while t >= 0:
        if pow(inv_a * (x ** 2), pow(2, t), p) != 1:
            x = x * pow(b, pow(2, base - t)) % p
            print('x_', t, '=', x)
        t -= 1

    return x


if __name__ == '__main__':
    # alst = [6, 14, 17, 19]
    # plst = [2011, 20190227]
    alst = [103]
    plst = [1601]
    for p in plst:
        for a in alst:
            x = solve_x_for_x2_equiv_a_mod_p(a, p)
            print(x, '^ 2 = ', a, ' mod ', p)
