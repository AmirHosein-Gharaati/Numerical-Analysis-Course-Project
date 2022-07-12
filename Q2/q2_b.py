import math
def newton_method(x0, f, f_prime):
    xi = x0
    x_next = 0
    for i in range(15):
        x_next = xi - (f(xi) / f_prime(xi))
    return '{:.4f}'.format(x_next), '{:.4f}'.format(abs(f(x_next)))


def g(x):
    return x ** 3 - math.sqrt(x ** 4 + x ** 2 + 5)


def g_prime(x):
    return (3 * x ** 2) - ((4 * x ** 3 + 2 * x) * ((x ** 4 + x ** 2 + 5) ** (-2 / 3))) / 3


res = []
i = 0.01
s = 0
min_ = float('inf')
while i < 3:
    temp = newton_method(i, g, g_prime)
    res += [(float(temp[0]), float(temp[1]))]
    if float(temp[1]) < min_:
        min_ = float(temp[1])
        s = float(temp[0])
    i += 0.01

print(min_)
print(s)
a = g(1.5298)
print(a)