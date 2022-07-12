import numpy as np

A = np.matrix([
    [9, -3, -6],
    [2, 8, 2],
    [-5, 10, 7]
])

x = np.matrix([
    [1],
    [1],
    [1]
])

n = 10


# Maximum --------------------------


# Positive
e_list_max = np.array([])

for i in range(1, n+1):
    new_x = np.matmul(A, x)
    e_list_max = np.append(e_list_max, new_x.max())
    x = np.divide(new_x, e_list_max[-1])

lambda_max_positive = e_list_max[-1]

print('Lambda Max Positive: ', lambda_max_positive)



e_list_max = np.array([])

for i in range(1, n+1):
    new_x = np.matmul(A, x)
    e_list_max = np.append(e_list_max, new_x.min())
    x = np.divide(new_x, e_list_max[-1])

lambda_max_negative = e_list_max[-1]

print('Lambda Max Negative: ', lambda_max_negative)


# Final result max
if abs(lambda_max_positive) > abs(lambda_max_negative):
    final_lambda_max = lambda_max_positive
else:
    final_lambda_max = lambda_max_negative

print(f"Final Lambda Max: {final_lambda_max}")

print('--------------------')


# ----------------------------------



A = np.matrix([
    [9, -3, -6],
    [2, 8, 2],
    [-5, 10, 7]
])

A_inverse = np.linalg.inv(A)

x = np.matrix([
    [1],
    [1],
    [1]
])

n = 10



# Minimum --------------------------


# Positive
e_list_min = np.array([])

for i in range(1, n+1):
    new_x = np.matmul(A_inverse, x)
    e_list_min = np.append(e_list_min, new_x.max())
    x = np.divide(new_x, e_list_min[-1])

inverse_lambda_min_positive = 1/e_list_min[-1]

print('Lambda Min Positive: ', inverse_lambda_min_positive)


# Negative
e_list_min = np.array([])

for i in range(1, n+1):
    new_x = np.matmul(A_inverse, x)
    e_list_min = np.append(e_list_min, new_x.min())
    x = np.divide(new_x, e_list_min[-1])

inverse_lambda_min_negative = 1/e_list_min[-1]

print('Lambda Min Negative: ', inverse_lambda_min_negative)


# Final result min
if abs(inverse_lambda_min_positive) > abs(inverse_lambda_min_negative):
    final_lambda_min = inverse_lambda_min_negative
else:
    final_lambda_min = inverse_lambda_min_positive

print(f"Final Lambda Min: {final_lambda_min}")