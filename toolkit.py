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
