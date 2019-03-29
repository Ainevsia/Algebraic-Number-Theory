p = 0xe5a111a219c64f841669400f51a54dd4e75184004f0f4d21c6ae182cfb528652a02d6d677a72b564c505b1ed42a0c648dbfe14eb66b04c0d60ba3872826c32e7
q = 0x98cb760764484e29245521be08e7f38edeebfca8427149524ba7f4735e1d5f3a45d585cb3722ff4c07c19165be738311dc346a914966f5b311416fed3b425079
n = p * q
phi = (p-1) * (q-1)
e = 65537

def cald(phi, e):
    s, t, sn, tn, r = 1, 0, 0, 1, 1
    while r!=0:
        q = phi // e
        r = phi - q * e
        st, tt = sn * (-q) + s, tn * (-q) + t
        s, t = sn, tn
        sn ,tn = st, tt
        phi = e
        e = r
    return t

# used to convert message to hex integers
def hexify(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        lst.append(hv)
    return '0x' + ''.join(lst)

d = cald(phi, e) % phi
a = input('please input the message you want to encrypt:') 
c = pow(eval(hexify(a)), e, n)
plaintext = hex(pow(c, d, n)).replace('0x', '')
if len(plaintext) % 2 == 1:
    plaintext = '0' + plaintext

def stringify(plaintext):
    lst = []
    end = len(plaintext) // 2
    for i in range(end):
        lst.append(chr(eval('0x' + plaintext[2*i: 2*(i+1)])))
    return ''.join(lst)

print(stringify(plaintext))
