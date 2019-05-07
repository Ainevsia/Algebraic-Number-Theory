from toolkit import Legendre

plst = [19, 17, 23]
for p in plst:
    is_redundant = []
    not_redundant = []
    for i in range(1, p):
        L = Legendre(i, p)
        if L == 1:
            is_redundant.append(i)
        else:
            not_redundant.append(i)
    print(p, '所有二次剩余:', is_redundant);
    print(p, '所有二次非剩余:', not_redundant)

alst = [2, 3, 17, 2011]
p = 2017
for a in alst:
    L = Legendre(a, p)
    print(L)
    if L == 1:
        print(a, '是模p平方剩余')
    else:
        print(a, '是模p平方非剩余')

# alst = [6, 14, 17, 19]
# plst = [2011, 2017, 20190221, 20190227]
# for p in plst:
#     for a in alst:
#         L = Legendre(a, p)
#         if L == 1:
#             print(a, '是模', p, '平方剩余')
#         else:
#             print(a, '是模', p, '平方非剩余') 