from math import sin, cos, exp
import numpy as np

f = lambda x : sin(31*x) - 2*cos(23*x)


# A)
a = []
b = []

n = 100
x = np.linspace(-7, 6.5, n)
    
for i in range(len(x)-1):
        
    if f(x[i]) * f(x[i+1]) < 0:
        a = np.append(a, x[i])
        b = np.append(b, x[i+1])
    elif f(x[i]) == 0:
        a = np.append(a, x[i])
        b = np.append(a, x[i])

if f(x[-1]) == 0:
    a = np.append(b, x[n-1])
    b = np.append(a, x[n-1])

print(f"length of a: {len(a)}, b: {len(b)}")
print()
for i in range(len(a)):
    print(f"{round(a[i], 3)}, {round(b[i], 3)}")


print('----------------------------------')





# B)
# Note: The result of every period is printed, so we have the same length of rows with previous section size

from tabulate import tabulate

x_n = lambda a, b: (a + b) / 2

round_digits = 2
result_xn = None
answers = []
step = 10

for j in range(len(a)):
    _a = a[j]
    _b = b[j]

    result_xn = None
    result_fa = None
    result_fxn = None
    sign = ''

    for i in range(1, step+1):

        result_xn = x_n(_a, _b)
        result_fa = f(_a)
        result_fxn = f(result_xn)
        sign = '+' if result_fa * result_fxn > 0  else '-'

        if result_fa * result_fxn == 0 :
            print("Zero Detected")

        if sign == '+':
            _a = result_xn
        else:
            _b = result_xn

    answers.append([j+1, _a, _b, result_xn, sign, result_fxn])


headers = ["Step", "a", "b", "xn", "Sign", "f_xn"]
table = tabulate(answers, headers, tablefmt="fancy_grid")

print(table)