from toolkit import *


def test():
    for i in prime[2:20]:
        print(i)
        print(sorted(root(i)))
        print(ori_root(i ** 2))
        print('=' * 20)


if __name__ == '__main__':
    # 29
    # [2, 3, 8, 10, 11, 14, 15, 18, 19, 21, 26, 27]
    # [2, 3, 8, 10, 11, 15, 18, 19, 21, 26, 27, 31,
    print(pow(14, phi(29 ** 2), 29 ** 2))
    print(pow(14, 28, 29 ** 2))
    for i in range(1, 29 ** 2):
        if pow(14, i, 29 ** 2) == 1:
            print(i)
            break
