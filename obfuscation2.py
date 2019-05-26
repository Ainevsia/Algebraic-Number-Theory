from capstone import *


def patch():
    md = Cs(CS_ARCH_X86, CS_MODE_64)
    c = open('/Users/xuqinxiang/Downloads/ctf/obfuscation2', 'rb').read()
    buffer = b''

    # virtual address base of the binary
    vdiff = 0x400000
    op = [None, None, None]

    # file offset of the target function
    rip = 0x4008BD - vdiff
    end = 0x400F35 - vdiff

    buffer += c[:rip]
    # print(buffer)
    cc = 0
    for i in md.disasm(c[rip:end], rip + vdiff):
        print("0x%x:\t%s\t%s" % (i.address, i.mnemonic, i.op_str))
        # print(i.bytes)
        # print(i.id)
        # print(type(i.id))
        if i.id == 224:
            cc += 1
            # buffer += b'\x48\x83\xC0\x01'
        else:
            if cc != 0:
                buffer += b'\x48\x83\xC0\x04'
                buffer += b'\x90' * cc
            buffer += i.bytes
            cc = 0
    # print("%x"%c[end])
    buffer += c[end:]
    open('/Users/xuqinxiang/Downloads/ctf/deobfuscated.raw', 'wb').write(buffer)


# if __name__ == '__main__':
#     patch()
input = '1234567890123456789012345678901234567\x00'
out = '\xa7\xfd\xfb\x8e\x57\x73\xdf\xe5\xec\xcc\xe8\x13\x39\xa5\x7a\xa8\x47\x68\x6b\xfe\xfe\x40\x08\x51\x97\xbe\x6f\xe0\x47\x42\x2a\x13\xa3\xf4\xc6\xe0\xbd\xf7'
# out = '\xc0\x66\x56\x56\x97\x2e\x31\xc8\x00\x71\xe4\x88\x70\x97\x05\x47\x85\xc8\x33\x8b\xec\x52\x02\x2a\xab\x27\x53\x69\xc2\xac\xaa\x1b\xce\xe3\x7f\x05\x2d\xb6'
# out = b'0xa7	0xfd	0xfb	0x8e	0x57	0x73	0xdf	0xe5 0xec	0xcc	0xe8	0x13	0x39	0xa5	0x7a	0xa8 0x47	0x68	0x6b	0xfe	0xfe	0x40	0x08	0x51 0x97	0xbe	0x6f	0xe0	0x47	0x42	0x2a	0x13 0xa3	0xf4	0xc6	0xe0	0xbd	0xf7'
# print(out.replace(b'\t', b''))
# out = '0xa70xfd0xfb0x8e0x570x730xdf0xe5 0xec0xcc0xe80x130x390xa50x7a0xa8 0x470x680x6b0xfe0xfe0x400x080x51 0x970xbe0x6f0xe00x470x420x2a0x13 0xa30xf40xc60xe00xbd0xf7'
# print(out.replace('0x', '\\x').replace(' ', ''))

# print(len(input), len(out))
en = [ord(a) ^ ord(b) for (a, b) in zip(input, out)]
for i in en:
    print('\\x{:02x}'.format(i), end='')
# test = '\x90\x0a\x33\x37\xe4\x4b\x31\xc8\xb2\x76\xa4\x88\x70\x97\x05\x47\x85\xc8\x33\x8b\xec\x52\x02\x2a\xab\x27\x53\x69\xc2\xac\xaa\x1b\xce\xe3\x7f\x05\x2d\x8e'
test = '\x96\xcf\xc8\xba\x62\x45\xe8\xdd\xd5\xfc\xd9\x21\x0a\x91\x4f\x9e\x70\x50\x52\xce\xcf\x72\x3b\x65\xa2\x88\x58\xd8\x7e\x72\x1b\x21\x90\xc0\xf3\xd6\x8a\xf7'

em = '''cmpstr[0] = 0x62;
  cmpstr[1] = 0x67;
  cmpstr[2] = 0xD5u;
  cmpstr[3] = 0xF3u;
  cmpstr[4] = 0xCEu;
  cmpstr[5] = 0x6F;
  cmpstr[6] = 0x56;
  cmpstr[7] = 0x67;
  cmpstr[8] = 0x18;
  cmpstr[9] = 0xB1u;
  cmpstr[0xA] = 0xC1u;
  cmpstr[0xB] = 0x4E;
  cmpstr[0xC] = 0x50;
  cmpstr[0xD] = 0x9Eu;
  cmpstr[0xE] = 0xB4u;
  cmpstr[0xF] = 0xCAu;
  cmpstr[0x10] = 0xCBu;
  cmpstr[17] = 0x3E;
  cmpstr[18] = 0x18;
  cmpstr[0x13] = 9;
  cmpstr[0x14] = 0x26;
  cmpstr[0x15] = 0x24;
  cmpstr[0x16] = 0x19;
  cmpstr[0x17] = 0x6B;
  cmpstr[0x18] = 0x5F;
  cmpstr[0x19] = 0xC2u;
  cmpstr[0x1A] = 0xF8u;
  cmpstr[27] = 0xE4u;
  cmpstr[0x1C] = 0x4C;
  cmpstr[0x1D] = 0xDFu;
  cmpstr[0x1E] = 0xA;
  cmpstr[0x1F] = 0xA4u;
  cmpstr[0x20] = 0x2C;
  cmpstr[0x21] = 0x8Bu;
  cmpstr[0x22] = 0x87u;
  cmpstr[0x23] = 0x98u;
  cmpstr[36] = 0xE0u;
  cmpstr[37] = 0x51;'''
import re
src = em
reobj = re.compile('cmpstr\[.*\] = ')
em = reobj.sub('', src)
print('hello')
print(em)

st = '''0x62;
  0x67;
  0xD5u;
  0xF3u;
  0xCEu;
  0x6F;
  0x56;
  0x67;
  0x18;
  0xB1u;
  0xC1u;
  0x4E;
  0x50;
  0x9Eu;
  0xB4u;
  0xCAu;
  0xCBu;
  0x3E;
  0x18;
  0x09;
  0x26;
  0x24;
  0x19;
  0x6B;
  0x5F;
  0xC2u;
  0xF8u;
  0xE4u;
  0x4C;
  0xDFu;
  0x0A;
  0xA4u;
  0x2C;
  0x8Bu;
  0x87u;
  0x98u;
  0xE0u;
  0x51;'''
print('hll')
print(st.replace(';\n','').replace('u','').replace(' ','').replace('0x','\\x'))
cmp = '\x62\x67\xD5\xF3\xCE\x6F\x56\x67\x18\xB1\xC1\x4E\x50\x9E\xB4\xCA\xCB\x3E\x18\x09\x26\x24\x19\x6B\x5F\xC2\xF8\xE4\x4C\xDF\x0A\xA4\x2C\x8B\x87\x98\xE0\x51'

print(len(cmp),len(test))
fs = [ord(a) ^ ord(b) for (a, b) in zip(cmp, test)]
for i in fs:
    print('{:2x}'.format(i), end='')
print('')
string = 'f4a81d49ac2abebacd4d186f5a0ffb54bb6e4ac7e956220efd4aa03c32ad1185bc4b744e6aa6'
# \x903\xb6\x91otP\x97!\xf0\x15\xf1\r=\x82\xb6x\xcc\x1f\xb3\xfeD(t\xc0\xae\x9c\xb2\xb7B\x91\x88\xd1\\\xcf\xab\xc7\xe7

import binascii
print(binascii.unhexlify(string))

# a = '\x00\xf4'
# b = '\xff\x00'
# fs = [ord(a) ^ ord(b) for (a, b) in zip(a, b)]
# for i in fs:
#     print('{:x}'.format(i), end='')