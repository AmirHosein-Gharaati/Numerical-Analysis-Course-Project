import numpy as np



def Cal_LU(D, g):
    A = np.array((D), dtype=float)
    f = np.array((g), dtype=float)
    n = f.size
    for i in range(0, n - 1):  # Loop through the columns of the matrix
        for j in range(i + 1, n):  # Loop through rows below diagonal for each column
            m = A[j, i] / A[i, i]
            A[j, :] = A[j, :] - m * A[i, :]
            f[j] = f[j] - m * f[i]

    return A, f


def Back_Subs(A, f):
    n = f.size
    x = np.zeros(n)
    x[n - 1] = f[n - 1] / A[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        sum_ = 0
        for j in range(i + 1, n):
            sum_ = sum_ + A[i, j] * x[j]
        x[i] = float(f[i] - sum_) / A[i, i]
    print("The Solution is: ")
    index = 0
    symboles = ['x', 'y', 'z', 'w', 'm']
    for t in x:
        print(symboles[index],'= {:.4f}'.format(t), end='     ')
        index += 1



A = np.array([[0.3, 9, -1, 3, -2],
              [7, 0, 1, -4, -1],
              [6, 2, 2, 8, 1],
              [-1, 17, -1.2, 1, 0],
              [-1, 1, 1, 2, 0]])

f = np.array([17, 3, 1, 15, -7])
B, g = Cal_LU(A, f)
Back_Subs(B, g)

