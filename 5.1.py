from toolkit import *

if __name__ == '__main__':
    plst = [17, 19, 21, pow(2, 4), pow(5, 2)]
    for p in plst:
        print('p =', p)
        simplified_redundant = []
        for i in range(1, p):
            if gcd(i, p) == 1:
                simplified_redundant.append(i)
        print('a\t|', end='')
        print(*simplified_redundant, sep='\t|')
        # the *-operator unpacks the list elements
        ordpa = []
        for a in simplified_redundant:  # range contains the first exclude the last
            ordpa.append(ord(p, a))
        print('ord\t|', end='')
        print(*ordpa, sep='\t|')
