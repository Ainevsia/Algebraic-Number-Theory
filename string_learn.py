x = 25
# x = str(x)
y = bytes([x,x])
print(len(y))
ds = b'\x48\x83\xC0\x04'
print(len(ds))
print(ds + y)