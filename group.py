p = 191
setlst = []
for g in [2, 7, 11, 19]:
	i = 1
	genlst = []
	while True:
		remain = pow(g, i, p)
		i += 1
		genlst.append(remain)
		if remain == 1:
			break
	genlst.sort()
	setlst.append(set(genlst))
	print('g =', g, '{', len(genlst), 'elements }')
	print(genlst)

s = set()
g = 7
H = [1, 7, 39, 49, 82, 109, 142, 152, 184, 190]
for i in range(1, 191):
	pj = [((c * i) % p) for c in H]
	pj.sort()
	s.add(str(pj))
print('number of peiji:', len(s))
cnt = 1
for i in s:
	print(cnt, '\t', i)
	cnt += 1

h = setlst[0]
k = setlst[1]
hk = list(set([((i * j) % p) for i in h for j in k]))
hjk = h & k
print(len(h), len(k), len(hk), len(hjk))
