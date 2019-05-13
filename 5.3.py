from toolkit import *

if __name__ == '__main__':
    plst = [17, 19, 191, 311, 313, 2011, 2017]
    for p in plst:
        print('p =', p)
        simplified_redundant = []
        for i in range(1, p):
            if gcd(i, p) == 1:
                simplified_redundant.append(i)
        # the *-operator unpacks the list elements
        ordpa = []
        for a in simplified_redundant:  # range contains the first exclude the last
            ordpa.append(ord(p, a))
        glst = []
        for i in range(len(simplified_redundant)):
            if ordpa[i] == phi(p):
                glst.append(simplified_redundant[i])
        print(glst)
