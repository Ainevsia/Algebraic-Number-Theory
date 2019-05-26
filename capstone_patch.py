from capstone import *
from capstone.x86 import *

md = Cs(CS_ARCH_X86, CS_MODE_64)
md.detail = True
code = open('/Users/xuqinxiang/Downloads/ctf/obfuscation2', 'rb').read()
buffer = b''

# virtual address base of the binary
vdiff = 0x400000
op = [None, None, None]

# file offset of the target function
rip = 0x4008BD - vdiff
end = 0x400F35 - vdiff

buffer += code[:rip]
switch = 0
cc = 0

while True:
    # disassemble one instruction
    i = md.disasm(code[rip:rip + 16], rip + vdiff)
    i = next(i)

    # increase rip
    rip += i.size

    #
    if switch == 1 and i.id == X86_INS_INT3:
        cc += 1
    elif i.id == X86_INS_MOV and 'al' in i.op_str and 'ptr' not in i.op_str:
        print("0x%x:\t%s\t%s" % (i.address, i.mnemonic, i.op_str))
        switch = 1
        for x in range(len(i.operands)):
            op[x] = i.operands[x]
    elif i.id == X86_INS_RET:
        buffer += i.bytes
        # print("0x%x:\t%s\t%s" % (i.address, i.mnemonic, i.op_str))
        break
    elif switch == 1 and i.id != X86_INS_INT3:
        switch = 0
        rv = (op[1].imm + cc)
        if rv >= 256:
            print('error'.center(3))
        rv %= 256
        buffer += b'\xb0' + bytes([rv]) + cc * b'\x90' + i.bytes
        cc = 0
    else:
        # print("0x%x:\t%s\t%s" % (i.address, i.mnemonic, i.op_str))
        buffer += i.bytes

# print("%x" % code[rip])
buffer += code[rip:]
# open('/Users/xuqinxiang/Downloads/ctf/capstone.obf', 'wb').write(buffer)

def test():
    print('-'*50)
    rip = 0x4008BD - vdiff
    # open('/Users/xuqinxiang/Downloads/ctf/capstone.obf', 'wb').write(buffer)
    for i in md.disasm(code[rip:end], rip + vdiff):
        print("0x%x:\t%s\t%s" % (i.address, i.mnemonic, i.op_str))
        # if i.id == 224:
        #     cc += 1
        # else:
        #     if cc >= 2:
        #         payload = b'\x14' + bytes([cc]) + b'\x90' * (cc - 2)
        #         buffer += payload
        #     elif cc == 1:
        #         buffer +=     b'\xcc'
        #     buffer += i.bytes
        #     cc = 0
    # print("%x"%c[end])
    # buffer += code[end:]
    # # open('/Users/xuqinxiang/Downloads/ctf/deobfuscated.2', 'wb').write(buffer)
# test()
