from Prime import prime
import csv


def phi(m):
    phi = 0
    if m in prime:
        phi = m - 1
    else:
        for i in range(1, m):
            if gcd(i, m) == 1:
                phi += 1
    return phi


def gcd(x, y):
    """
    Python code to demonstrate naive method to compute gcd, Euclidean algo
    """
    while (y):
        x, y = y, x % y
    return x


def ord(m, a):
    ret = 0
    for e in range(1, phi(m) + 1):
        if pow(a, e, m) == 1:
            ret = e
            break
    return ret


def write_gk_table(gk, p):
    with open("gk.csv", "w", newline="") as datacsv:
        # dialect为打开csv文件的方式，默认是excel，delimiter="\t"参数指写入的时候的分隔符
        csvwriter = csv.writer(datacsv, dialect=("excel"))
        # csv文件插入一行数据，把下面列表中的每一项放入一个单元格（可以用循环插入多行）
        csvwriter.writerow(['k', 'g^k'])
        for i in range(p - 1):
            csvwriter.writerow([i, gk[i]])


def Legendre(a, p):
    """
    p must be a prime number and (a, p) = 1
    calculate the Legendre of (a/p), ie, x^2 = a (mod p) solve or not
    """
    if p not in prime and p < 9973:
        print("p is not a prime number.")
        return 0
    a = a % p
    if a == 2:
        return 1 if ((pow(p, 2) - 1) / 8) % 2 == 0 else -1
    elif a == 1:
        return 1
    elif a == 0:
        return 0
    else:
        # take into consideration when 2 | a
        ls = factor(a)
        if ls[0] == 2:
            return Legendre(2, p) * Legendre(a // 2, p)
        else:
            return 1 if T(a, p) % 2 == 0 else -1


def T(a, p):
    """
    the number of dots in tri-angle down
    """
    ret = 0
    ed = (p + 1) >> 1
    for i in range(ed):
        ret += a * i // p
    return ret


def inverse_a_mod_p(a, p):
    """
    Use the Bezout law to calculate the inverse of e to the modulus of phi.
    """
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


def factor(m, repeat=True):
    factorls = []
    idx = 0
    while prime[idx] <= m:
        i = prime[idx]
        div, mod = divmod(m, i)
        if mod == 0:
            m //= i
            factorls.append(i)
        else:
            idx += 1
    return factorls if repeat else list(set(factorls))


def Jacobi(a, m):
    if m > prime[-1]:
        flag = 1 if ~((a - 1) // 2 & 1) | ~((m - 1) // 2 & 1) else -1
        return flag * Jacobi(m, a)

    factorls = factor(m)
    ret = 1
    for i in factorls:
        ret *= Legendre(a, i)
    return ret


def simplified_redundant(m):
    ls = []
    for i in range(1, m):
        if gcd(i, m) == 1:
            ls.append(i)
    return ls


def root(p):
    if p == 2:
        print('2 does not have root.')
        return 0
    if p not in prime and p < prime[-1]:
        print('p is not a prime number.')
        return 0
    exponent = [p // pi for pi in factor(phi(p), repeat=False)]
    roottestls = [2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29]
    found = False
    g = 0

    # find the first root
    for rt in roottestls:
        for expo in exponent:
            if pow(rt, expo, p) == 1:
                break
            if expo == exponent[-1]:
                g = rt
                found = True
        if found:
            break

    # find all the roots
    rootls = []
    for sim_redun in simplified_redundant(p - 1):
        rootls.append(pow(g, sim_redun, p))
    return rootls
