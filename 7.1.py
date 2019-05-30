# class Rational():
#     def __init__(self):
#

print('i\ta_i\t' + 'P_i/Q_i'.ljust(20) + ' diff')
P_nm2, P_nm1, Q_nm2, Q_nm1, P_n, Q_n = 0, 1, 1, 0, 0, 0
lst = []
n = 3.141592654
# n = 7700 / 2145
# n = (pow(5, 0.5) + 1) / 2
ori_n = n
for i in range(10):
    a = int(n)
    lst.append(a)
    P_n, Q_n = a * P_nm1 + P_nm2, a * Q_nm1 + Q_nm2
    P_nm2, P_nm1, Q_nm2, Q_nm1 = P_nm1, P_n, Q_nm1, Q_n
    x = n - a
    print(i, '\t', a, '\t', (str(P_n) + '/' + str(Q_n)).ljust(20), ' ' if ori_n - P_n / Q_n > 0 else '','{0:0.9f}'.format(ori_n - P_n / Q_n), sep='')
    if x > 1e-8:
        n = 1 / x
    else:
        break
print(lst)
