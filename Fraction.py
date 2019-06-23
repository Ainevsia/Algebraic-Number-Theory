from toolkit import *

nlst = [47 * 67, 2011 * 2017]
for n in nlst:
    p, q, Pk = [0], [1], [1]
    alpha = pow(n, 0.5)
    cnt = 1
    while True:
        a = int(alpha)
        p.append(a * q[-1] - p[-1])
        q.append((n - pow(p[-1], 2)) // q[-1])
        alpha = (p[-1] + pow(n, 0.5)) / q[-1]
        Pk.append(Pk[-1] * a + (Pk[-2] if cnt >= 2 else 0))
        # print(Pk)
        if cnt & 1 == 0 and pow(int(pow(q[-1], 0.5)), 2) == q[-1]:
            s = int(pow(q[-1], 0.5))
            # print(Pk[-1], s)
            factor = [gcd(Pk[-1] - s, n), gcd(Pk[-1] + s, n)]
            if factor[0] != 1 and factor[1] != 1:
                print('factor : %d,%d' % (factor[0], factor[1]))
                break
        cnt += 1
