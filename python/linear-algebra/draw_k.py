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
