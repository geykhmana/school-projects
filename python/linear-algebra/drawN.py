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
            ax1.plot([N[0, i], N[0, j], N[1, i], N[1, j], 'b'])
ax1.axis("off")
show()
plt.savefig("n-plot.png")
