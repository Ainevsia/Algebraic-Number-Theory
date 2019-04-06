"""
Use the Eratoshenes Algorithm to generate first 1229 prime numbers.
"""
max = 10000
smax = 100  # sqrt(10000)
lst = []  # number list, all True (is prime) at first
for i in range(max + 1):  # initialization
    lst.append(True)

for i in range(2, smax + 1):  # Eratoshenes Algorithm
    sieve = 2 * i
    while sieve <= max:
        lst[sieve] = False
        sieve += i

for i in range(2, max + 1):  # output in a line
    if lst[i] == True:
        print(i, end=',')
