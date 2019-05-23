from toolkit import *

plst = [17, 19, 191, 311, 313, 2011, 2017]
for p in plst:
    print('p = ', p)
    g = root(p, first=True)
    print('g = ', g)
    # print(pow(g, p - 1), pow(g + p, p - 1), pow(p, 2))
    g2 = g if pow(g, p - 1, p) == 1 else g + p
    print('g2 = ', g2)
    print('-' * 100)
