import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, ion, show

matplotlib.use("tkagg")

ion()
N = np.matrix([[0, 0.5, 0.5, 6, 6, 5.5, 5.5, 0],
               [0, 0, 6.42, 0, 8, 8, 1.58, 8]])
adj = np.matrix([[0, 1, 0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 0, 0, 0, 0],
                 [0, 1, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 1, 0],
                 [0, 0, 0, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1, 0]])

f1, ax1 = plt.subplots(1)
for i in range(8):
    for j in range(i + 1):
        if adj[i, j] == 1:
            ax1.plot([N[0, i], N[0, j]], [N[1, i], N[1, j]], 'b')

ax1.axis("off")
show()
plt.savefig("n-plot.png")

A = np.matrix([[1, 0.25], [0, 1]])  # Shear
SN = A * N
f2, ax2 = plt.subplots(1)

for i in range(8):
    for j in range(i + 1):
        if adj[i, j] == 1:
            ax2.plot([SN[0, i], SN[0, j]], [SN[1, i], SN[1, j]], 'b')

ax2.axis("off")
show()
plt.savefig("n-plot-transformed.png")

phi = math.pi / 6
R = np.matrix([[math.cos(phi), -math.sin(phi)],
               [math.sin(phi), math.cos(phi)]])
NR = R * N

f5, ax5 = plt.subplots(1, 2)
for i in range(8):
    for j in range(i + 1):
        if adj[i, j] == 1:
            ax5[0].plot([N[0, i], N[0, j]], [N[1, i], N[1, j]], "r")
            ax5[1].plot([NR[0, i], NR[0, j]], [NR[1, i], NR[1, j]], "b")
ax5[0].axis("off")
ax5[1].axis("off")
ax5[0].set_title("Regular N")
ax5[1].set_title("Rotated N")
plt.savefig("RegularAndRotatedN.png")
