from random import Random


def random_str(randomlength):
    ret_str = ''
    chars = 'abcdef0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        ret_str += chars[random.randint(0, length)]
    return ret_str


from Prime import prime
from FermatTest import fermat_test


def random_prime():
    while True:
        ran_int = eval('0x' + random_str(256))
        if ran_int & 1 == False:
            ran_int += 1
        notprime = False
        for i in range(len(prime)):
            if ran_int % prime[i] == 0:
                notprime = True
                break
        if notprime:
            pass
        elif fermat_test(ran_int, 16) == False:
            pass
        else:
            return ran_int
