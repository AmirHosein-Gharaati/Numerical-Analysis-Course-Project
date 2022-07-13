def f(x):
    return x ** 3 + 4 * x ** 2 - 2

def bisection_method(a, b, f):
    step = 1
    xn = (a + b) / 2
    print(f(xn))
    print('---------------------------')
    while True:
        if abs(f(xn)) <= 0.004: return step, xn, f(xn)
        if f(a) * f(xn) > 0:
            a = xn
        else:
            b = xn

        xn = (a + b) / 2
        step += 1
        print('xn = {:.3f}'.format(xn))
        print('f(xn) * f(a) ={:.3f}'.format(f(xn) * f(a)))
        print('f(xn) = {:.3f}'.format(f(xn)))
        print('-------------------------')


res = bisection_method(0, 1, f)
step = res[0]
print('xn =', '{:.4f}'.format(res[1]))
print('f_xn =', '{:.4f}'.format(res[2]))
print('We Calculate this answer after',step,'step')








