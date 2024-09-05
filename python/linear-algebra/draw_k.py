import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, ion, show

matplotlib.use("tkagg")

ion()
k = np.matrix([[0, 0, 0.7, 0.7, 4, 5, 1.4, 5, 4, 0.7, 0.7],
               [0, 10, 10, 4.25, 6.5, 6.5, 4, 0, 0, 3.6, 0]])
adj = np.matrix([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]])

f1, ax1 = plt.subplots(1)
for i in range(11):
    for j in range(i + 1):
        if adj[i, j] == 1:
            ax1.plot([k[0, i], k[0, j]], [k[1, i], k[1, j]], 'b')

plt.xlim(0, 12)
plt.ylim(0, 10)
ax1.axis("off")
ax1.set_title("Regular k")
show()
plt.savefig("k-plot.png")

phi = math.pi / 4
R = np.matrix([[math.cos(phi), -math.sin(phi)],
               [math.sin(phi), math.cos(phi)]])
kR = R * k

f2, ax2 = plt.subplots(1)
for i in range(11):
    for j in range(i + 1):
        if adj[i, j] == 1:
            ax2.plot([kR[0, i], kR[0, j]], [kR[1, i], kR[1, j]], "b")

ax2.axis("off")
ax2.set_title("Rotated k")
plt.savefig("rotated-k-plot.png")

T = np.matrix([[-1, 0],
               [0, 1]])
kT = T * k

f5, ax5 = plt.subplots(1, 2)
for i in range(11):
    for j in range(i + 1):
        if adj[i, j] == 1:
            ax5[0].plot([k[0, i], k[0, j]], [k[1, i], k[1, j]], "r")
            ax5[1].plot([kT[0, i], kT[0, j]], [kT[1, i], kT[1, j]], "b")
ax5[0].axis("off")
ax5[1].axis("off")
ax5[0].set_title("Regular k")
ax5[1].set_title("Reversed k")
plt.savefig("regular-and-reversed-k-plots.png")
