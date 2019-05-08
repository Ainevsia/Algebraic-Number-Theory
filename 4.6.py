from toolkit import *

if __name__ == '__main__':
    plst = [2011, 20190221]
    qlst = [2017, 20190227]
    mlst = [plst[i] * qlst[i] for i in range(2)]
    alst = [6, 14, 17, 19]
    for m in mlst:
        for a in alst:
            print('Jacobi(', a, '/', m, ') = ', Jacobi(a, m))
    lst = [3, 5, 7]
    for i in lst:
        print('Legendre(', i, '/', 2017, ') = ', Legendre(i, 2017))
