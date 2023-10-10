import numpy as np

A = np.array([[2.2, 0.4, 9], [-1.2, 3.5, 7]])
B = np.array([[1.5, 19], [-1, 3.5], [4.5, 8]])

print(A @ B)
print(np.matmul(A, B))
print(A+1)