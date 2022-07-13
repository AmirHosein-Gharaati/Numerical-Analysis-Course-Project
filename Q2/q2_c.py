import math


def regular_falsi_method(a, b, f):
    xi = b - (((b - a) / (f(b) - f(a))) * f(b))
    if f(xi) * f(a) > 0:
        a = xi
    else:
        b = xi
    step = 1

    while True:
        step += 1
        if abs(f(xi)) < 0.001: return xi, step
        xi = b - (((b - a) / (f(b) - f(a))) * f(b))
        a = xi


def f(x):
    return x ** 3 - 2 ** (math.sqrt(x))


res = regular_falsi_method(1, 2, f)
xi = res[0]
step = res[1]
print('{:.4f}'.format(f(xi)))
print('step = ', step)