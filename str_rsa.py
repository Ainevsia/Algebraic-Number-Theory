def inverse(phi, e):
    """
    Use the Bezout law to calculate the inverse of e to the modulus of phi.

    :param phi:
    :param e:
    :return:
    """
    s, t, sn, tn, r = 1, 0, 0, 1, 1
    while r != 0:
        q = phi // e
        r = phi - q * e
        st, tt = sn * (-q) + s, tn * (-q) + t
        s, t = sn, tn
        sn, tn = st, tt
        phi = e
        e = r
    return t


def hexify(s):
    """
    Used to convert message to hex integers.

    :param s:
    :return: 
    """
    if not s:
        return '0x21'
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        lst.append(hv)
    return '0x' + ''.join(lst)


def stringify(plaintext):
    lst = []
    end = len(plaintext) // 2
    for i in range(end):
        lst.append(chr(eval('0x' + plaintext[2 * i: 2 * (i + 1)])))
    return ''.join(lst)