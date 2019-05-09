from toolkit import *

if __name__ == '__main__':
    ls = [113, 167, 2017]
    for i in ls:
        print(i, root(i), phi(i - 1), len(root(i)))
