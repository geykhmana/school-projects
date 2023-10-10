import numpy as np

A = np.array([[2.2, 0.4, 9], [-1.2, 3.5, 7]])
B = np.array([[1.5, 19], [-1, 3.5], [4.5, 8]])
I3 = np.eye(3, 3)  # 3x3 identity matrix
D = np.array([[1, 0, 3], [-2, 4, 1], [10, 5, -2.7]])

print(A @ B)
print(np.matmul(A, B))
print(A + 1)  # Adds 1 to every entry
print(I3)
print(A.T)  # Transposes the matrix
print(B.T)
print(np.linalg.inv(D))
print(np.multiply(A, A))  # Only works on matrices of the same size
print(A / A)
