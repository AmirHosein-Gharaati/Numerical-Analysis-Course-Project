import math


def f(x):
    return x ** 3 - math.sqrt(x ** 4 + x ** 2 + 5)


# Defining derivative of function
def g(x):
    return (3 * x ** 2) - ((4 * x ** 3 + 2 * x) * ((x ** 4 + x ** 2 + 5) ** (-2 / 3))) / 3


# Implementing Newton Method

def newton_method(x0, e, N):
    step = 1
    flag = 1
    i = 0
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Divide by zero error!')
            break

        x1 = x0 - f(x0) / g(x0)
        print('n:%d, x%i = %0.6f and f(x%i) = %0.6f' % (step, i, x1, i, f(x1)))
        x0 = x1
        step = step + 1

        if step > N:
            flag = 0
            break

        condition = abs(f(x1)) > e
        i += 1

    if flag == 1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')


# Input Section
x0 = input('Enter Guess: ')
e = input('Tolerable Error: ')
N = input('Maximum Step: ')

# Converting x0 and e to float
x0 = float(x0)
e = float(e)

# Converting N to integer

N = int(N)


x0 = float(input('Enter Guess: '))
e = float(input('Tolerable Error: '))
N = int(input('Maximum Step: '))

# Starting Newton Method
newton_method(x0, e, N)
