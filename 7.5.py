# from toolkit import *
from math import sqrt, floor, gcd

# use this package to represent rational numbers and the result can be accurate

m = 47 * 67
m=1037
n = m ** 0.5
print('n =', n)
print('k\ta_i\t' + 'P_i'.ljust(20))
P_nm2, P_nm1, Q_nm2, Q_nm1, P_n, Q_n = 0, 1, 1, 0, 0, 0
lst = []
plst, qlst, factorlst = [], [], []
ori_n = n
for i in range(30):
    a = int(n)
    lst.append(a)
    P_n, Q_n = a * P_nm1 + P_nm2, a * Q_nm1 + Q_nm2
    P_nm2, P_nm1, Q_nm2, Q_nm1 = P_nm1, P_n, Q_nm1, Q_n
    x = n - a
    plst.append(P_n)

    factorlst.append((pow(P_n, 2, m)))
    print(i, '\t', a, '\t', str(P_n).ljust(30),str(Q_n).ljust(20), sep='')
    if i & 1 == 0 and i != 0 and int(sqrt(Q_n)) * int(sqrt(Q_n)) == Q_n:
        s = int(Q_n ** 0.5)
        print(s)
        if True:
            print('第%d项：%d,%d' % (i, gcd(P_nm2 - s, m), gcd(P_nm2 + s, m)))
            print('程序运行完毕！')
            # break

    if x > 1e-5:
        n = 1 / x
    else:
        break
# print('continued fraction :', lst)
# for i in range(len(factorlst)):
#     for j in range(i + 1, len(factorlst)):
#         if factorlst[i] == factorlst[j]:
#             print(i, j)
#             x = plst[i] * plst[j]
#             y = factorlst[i]
#             if gcd(x + y, m) == m:
#                 continue
#             else:
#                 print(gcd(x + y, m), gcd(x - y, m))

# x = plst[i]
# y = gcd(plst[i], plst[j])
# if gcd(x + y, m) == m or gcd(x + y, m) == 1:
#     continue
# else:
#     print(gcd(x + y, m), gcd(x - y, m))
