import numpy as np

A = np.array([[2.2, 0.4, 9], [-1.2, 3.5, 7]])
B = np.array([[1.5, 19], [-1, 3.5], [4.5, 8]])
I3 = np.eye(3, 3)  # 3x3 identity matrix
D = np.array([[1, 0, 3], [-2, 4, 1], [10, 5, -2.7]])
C1 = np.matrix('10, 5, -2.7; 10, 5, -2.7; 10, 5, -2.7')
C2 = np.array([[10, 5, -2.7], [10, 5, -2.7], [10, 5, -2.7]])
A1 = np.matrix('2.2, 0.4, 9; -1.2, 3.5, 7')
B1 = np.matrix('1.5, 19; -1, 3.5; 4.5, 8')
D1 = np.matrix(D)  # Converts an array to a matrix
u = np.matrix('3; 0; 7')
v = np.matrix('34; 119')

print(A @ B)
print(np.matmul(A, B))
print(A + 1)  # Adds 1 to every entry
print(I3)
print(A.T)  # Transposes the matrix
print(B.T)
print(np.linalg.inv(D))
print(np.multiply(A, A))  # Only works on matrices of the same size
print(A / A)
print(D / D[2, :])
print(C1)
print(D / C2)
print(A - A1)
print(B - B1)
print(D1)
print(B1.T * D1)
print(A1*3*u - 2*v)
