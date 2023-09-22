import numpy as np

A = np.array([[8.0, 3, -2], [-4, 7, 5], [3, 4, -12]])
b = np.array([[9.0], [15], [35]])
Ans1 = np.linalg.solve(A, b)
print(Ans1)

A1 = np.matrix('1.0 , 1, 1; 1, 2, 4; 1, 3, 9')
b1 = np.matrix('12.0; 15; 16')
Ans2 = np.linalg.solve(A1, b1)
print(Ans2)

Ag = np.matrix([[1.0, 1, 1, 12], [1, 2, 4, 15], [1, 3, 9, 19]])
print(Ag[0,0])
print(Ag[0,2])
print(Ag[0,:])
print(Ag[1,:])
print(Ag[:, 3])