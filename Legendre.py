from Prime import prime 

def Legendre(a, p):
    """
    p must be a prime number and (a, p) = 1
    calculate the Legendre of (a/p), ie, x^2 = a (mod p) solve or not
    """
    if p not in prime and p < 9973:
        print("p is not a prime number.")
        return 0
    a = a % p
    if a == 2:
        return 1 if ((pow(p, 2)-1)/8)%2==0 else -1
    elif a == 1:
        return 1
    elif a == 0:
        return 0
    else:
        return 1 if T(a, p)%2==0 else -1 


def T(a, p):
    """
    the number of dots in tri-angle down
    """
    ret = 0
    ed  = (p + 1)>>1
    for i in range(ed):
       ret += a * i // p
    return ret


# a = eval(input('please input a:'))
# p = eval(input('please input p:'))
cnt = 0
for p in [17, 31]:
    for i in range(p):
        cnt += 1
        a = i**3 + 4 
        print('\n\n====round ' + str(cnt) + ' p = {}, x = {}===='.format(p, i))
        Legend = Legendre(a, p)
        print('({}/{}) = '.format(a, p), Legend)
        if Legend == -1:
            print('it means x^2 = {} mod {} has no solution'.format(a, p))
        else:
            print('it means x^2 = {} mod {} do have solution'.format(a, p))
            for i in range(p):
                remain = a % p
                if pow(i,2,p) == remain:
                    print('one root is', i)
