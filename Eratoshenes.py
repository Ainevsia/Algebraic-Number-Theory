max = 10000
smax = 100
cnt = 0
lst = []
for i in range(max + 1):
    lst.append(True)
for i in range(2, smax + 1):
    sieve = 2 * i
    while sieve <= max:
        lst[sieve] = False
        sieve += i
for i in range(2, max + 1):
    if lst[i] == True:
        print(i, end=',')
        cnt += 1
print(cnt)
