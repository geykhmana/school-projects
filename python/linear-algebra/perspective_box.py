import math
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from matplotlib.pyplot import plot, ion, show

ion()
matplotlib.use("tkagg")  # Mac only

D = np.matrix([[3, 5, 5, 3, 3, 5, 5, 3], [1, 1, 0, 0, 1, 1, 0, 0],
               [5, 5, 5, 5, 4, 4, 4, 4], [1, 1, 1, 1, 1, 1, 1, 1]])
C = np.matrix([[0, 1, 0, 1, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1, 0, 0],
               [0, 1, 0, 1, 0, 0, 1, 0], [1, 0, 1, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 1, 0, 1], [0, 1, 0, 0, 1, 0, 1, 0],
               [0, 0, 1, 0, 0, 1, 0, 1], [0, 0, 0, 1, 1, 0, 1, 0]])

b, c, d = 10, 5, 10  # center
center = (b, c, d)
P = np.matrix([[1, 0, -b / d, 0], [0, 1, -c / d, 0], [0, 0, 0, 0], [0, 0, -1 / d, 1]])
PD = P * D
PD = PD / PD[3, :]

f, ax = plt.subplots(1)

for i in range(8):
    for j in range(i + 1):
        if C[i, j] == 1:
            ax.plot([PD[0, i], PD[0, j]], [PD[1, i], PD[1, j]], "g")

ax.set_title("Center at " + str(center))
ax.axis("off")
plt.savefig("PerspectiveBox.png")
