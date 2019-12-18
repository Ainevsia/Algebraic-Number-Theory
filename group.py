p = 191
setlst = []
print("这个程序展示了素数191的简化剩余系作为循环交换群时的一些性质\n")
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
	print('由元素 g =', g, '所生成的循环群的元素个数 {', len(genlst), 'elements }')
	print("循环群元素：")
	print(genlst)
	print('\n')

s = set()
g = 7
H = [1, 7, 39, 49, 82, 109, 142, 152, 184, 190]
for i in range(1, 191):
	pj = [((c * i) % p) for c in H]
	pj.sort()
	s.add(str(pj))
print('陪集个数:', len(s))
cnt = 1
print("商集元素列举")
for i in s:
	print(cnt, '\t', i)
	cnt += 1

# h = setlst[0]
# k = setlst[1]
# hk = list(set([((i * j) % p) for i in h for j in k]))
# hjk = h & k
# print(len(h), len(k), len(hk), len(hjk))
