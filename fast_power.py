def fast_power(b, n, m):
    a = 1
    while n:
        if n & 1:
            a = (a * b) % m
        b = (b * b) % m
        n //= 2
    return a

b = 9823423237346355553453453524524532332
n = 3333
m = 73342323425555345345352452232

print(pow(b, n, m))
ret = fast_power(b, n, m)
print(ret)
