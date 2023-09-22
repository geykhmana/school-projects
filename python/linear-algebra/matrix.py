import numpy as np

A = np.array([[8.0, 3, -2], [-4, 7, 5], [3, 4, -12]])
b = np.array([[9.0], [15], [35]])
Ans1 = np.linalg.solve(A, b)
print(Ans1)