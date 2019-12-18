import collections

# use two args to denote a elliptic curve
ECC = collections.namedtuple('ECC_E', ['a4', 'a6'])
E = ECC(a4=3, a6=1)

# namedtuple to represent a point on E
P = collections.namedtuple('ECC_Point', ['x', 'y'])
P1 = P(x=1,y=1)

def add(E, P, Q):
    