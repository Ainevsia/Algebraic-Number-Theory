from toolkit import *

nlst = [1105, 1729]
for n in nlst:
    error = False
    blst = simplified_redundant(n)
    for b in blst:
        if pow(b, n-1, n) != 1:
            error = True
    if error:
        print(n,'is not a Carmichael number')
    else:
        print(n, 'is a Carmichael number')
