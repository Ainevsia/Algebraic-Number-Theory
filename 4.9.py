
def solve_x_y_for_x2_plus_y2_equals_p(p):
    div, mod = divmod(p - 5, 8)
    if mod != 0:
        print('p is not a prime number like 8k+5')
        return 0, 0
    x, y = pow(2, (p - 1) // 4, p), 1
    m = (pow(x, 2) + 1) // p
    while m != 1:
        u, v = x % m, y % m
        x, y = (u * x + v * y) // m, (u * y - v * x) // m
        m = (pow(x, 2) + pow(y, 2)) // p
    return x, y


if __name__ == '__main__':
    plst = [2017, 20190221]
    for p in plst:
        x, y = solve_x_y_for_x2_plus_y2_equals_p(p)
        if x ** 2 + y ** 2 == p:
            print(x, '^2 + ', y, '^2 = ', p)
