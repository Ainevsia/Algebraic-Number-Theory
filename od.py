from toolkit import *

p = 31
phi = phi(p)

if __name__ == '__main__':
    simplified_redundant = []
    for i in range(1, p):
        if gcd(i, p) == 1:
            simplified_redundant.append(i)
    print(simplified_redundant)
    ordpa = []
    for a in simplified_redundant:  # range contains the first exclude the last
        ordpa.append(ord(p, a))
    print(ordpa)
    glst = []
    for i in range(len(simplified_redundant)):
        if ordpa[i] == phi:
            glst.append(simplified_redundant[i])
    print(glst)
    g = glst[0]
    gk = []
    for k in range(p - 1):
        gk.append(pow(g, k, p))
    print(gk)
    # write_gk_table(gk, p)

    alst = [11, 11, 17]
    blst = [19, 20, 19]
    for a in alst:
        for b in blst:
            guv_idx = (gk.index(a) + gk.index(b)) % (p - 1)
            guv = gk[guv_idx]
            if guv ==a * b % p:
                print('√',end='')
            else:
                print('×', end='')
