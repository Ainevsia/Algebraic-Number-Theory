def inverse(phi, e):
    """
    Use the Bezout law to calculate the inverse of e to the modulus of phi.

    :param phi:
    :param e:
    :return: an integer d st. d*e = 1 (mod phi)
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
    Used to convert message to hex integers when encrypting.

    :param s: a string.
    :return: a string like '0x..', decode each character as a ascii hex number.
    """
    if not s:  # if input is null, evcrypt the message: '!'
        return '0x21'  # ascii code for '!'
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        lst.append(hv)
    return '0x' + ''.join(lst)


def stringify(plaintext):
    """
    Used to convert hex integers into a string when decrypting.

    :param plaintext: a hex integer number.
    :return: a ascii string.
    """
    if len(plaintext) % 2 == 1:
        plaintext = '0' + plaintext
    lst = []
    end = len(plaintext) // 2
    for i in range(end):
        lst.append(chr(eval('0x' + plaintext[2 * i: 2 * (i + 1)])))
    return ''.join(lst)
