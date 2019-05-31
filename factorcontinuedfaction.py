# -*- coding: utf-8 -*-
from math import sqrt, floor, gcd


# 判断是否为平方数
def is_square(n):
    t = int(sqrt(n))
    return t * t == n


def main():
    n = 2 ** 67 - 1  # 要分解的数
    n = 47 * 67
    print('n=%s' % ('2**67-1'))
    seq_P, seq_Q = 0, 1
    a0 = floor(sqrt(n))
    seq_a = [a0]
    seq_p = [0, a0]
    i = 1
    while True:
        # P_{k},Q_{k}序列
        seq_P = seq_a[0] * seq_Q - seq_P
        seq_Q = divmod(n - seq_P ** 2, seq_Q)[0]
        t = (seq_P + sqrt(n)) / seq_Q
        seq_a[0] = floor(t)
        # p_{k}序列
        if i == 1:
            seq_p.append(a0 * seq_a[0] + 1)
        else:
            seq_p[0] = seq_p[1]
            seq_p[1] = seq_p[2]  # this is P_n
            seq_p[2] = seq_a[0] * seq_p[1] + seq_p[0]
        # 分解因式
        if i % 2 == 0 and is_square(seq_Q):
            s = int(sqrt(seq_Q))
            factor = [gcd(seq_p[1] - s, n), gcd(seq_p[1] + s, n)]
            if factor[0] != 1 and factor[1] != 1:
                print('第%d项：%d,%d' % (i, factor[0], factor[1]))
                print('程序运行完毕！')
                break
        if i % 1000 == 0:
            print('已运行到第%d项' % i)
        i += 1


main()
