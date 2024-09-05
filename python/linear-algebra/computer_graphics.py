import math
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from matplotlib.pyplot import plot, ion, show

ion()
matplotlib.use("tkagg")  # Mac only

D = np.matrix([[-6.5, -6.5, -6.5, -6.5, -2.5, -2.5, -0.75, -0.75, 3.25, 3.25, 4.5, 4.5, 6.5, 6.5, 6.5, 6.5],
               [-2, -2, 0.5, 0.5, 0.5, 0.5, 2, 2, 2, 2, 0.5, 0.5, 0.5, 0.5, -2, -2],
               [-2.5, 2.5, 2.5, -2.5, -2.5, 2.5, -2.5, 2.5, -2.5, 2.5, -2.5, 2.5, -2.5, 2.5, 2.5, -2.5],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

C = np.matrix([[0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]])

b, c, d = -5, 10, 10  # center
center = (b, c, d)
P = np.matrix([[1, 0, -b / d, 0], [0, 1, -c / d, 0], [0, 0, 0, 0], [0, 0, -1 / d, 1]])
PD = P * D
PD = PD / PD[3, :]

f1, ax1 = plt.subplots(1)

for i in range(16):
    for j in range(i + 1):
        if C[i, j] == 1:
            ax1.plot([PD[0, i], PD[0, j]], [PD[1, i], PD[1, j]], "g")

ax1.set_title("Center at " + str(center))
ax1.axis("off")
plt.savefig("Toyota_-5_10_10.png")

b, c, d = 0, 10, 25  # center
center = (b, c, d)
P = np.matrix([[1, 0, -b / d, 0], [0, 1, -c / d, 0], [0, 0, 0, 0], [0, 0, -1 / d, 1]])
PD = P * D
PD = PD / PD[3, :]

f2, ax2 = plt.subplots(1)

for i in range(16):
    for j in range(i + 1):
        if C[i, j] == 1:
            ax2.plot([PD[0, i], PD[0, j]], [PD[1, i], PD[1, j]], "g")

ax2.set_title("Center at " + str(center))
ax2.axis("off")
plt.savefig("Toyota_0_10_25.png")

phi = math.pi / 6
R = np.matrix([[math.cos(phi), 0,  math.sin(phi), 0],
               [0, 1, 0, 0],
               [-math.sin(phi), 0, math.cos(phi), 0],
               [0, 0, 0, 1]])
RD = R * D
b, c, d = 0, 10, 25  # center
center = (b, c, d)
P = np.matrix([[1, 0, -b / d, 0], [0, 1, -c / d, 0], [0, 0, 0, 0], [0, 0, -1 / d, 1]])
PD = P * D
PD = PD / PD[3, :]
PRD = P * RD
PRD = PRD / PRD[3, :]

f3, ax3 = plt.subplots(1, 2)
for i in range(16):
    for j in range(i + 1):
        if C[i, j] == 1:
            ax3[0].plot([PD[0, i], PD[0, j]], [PD[1, i], PD[1, j]], "g")
            ax3[1].plot([PRD[0, i], PRD[0, j]], [PRD[1, i], PRD[1, j]], "r")
ax3[0].axis("off")
ax3[1].axis("off")
ax3[0].set_title("Center at " + str(center))
ax3[1].set_title("Rotated 30° about the y axis")
plt.savefig("Toyota_Normal_and_Rotated_30y.png")

phi = math.pi / 4
R = np.matrix([[math.cos(phi), -math.sin(phi),  0, 0],
               [math.sin(phi), math.cos(phi), 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1]])
RD = R * D
b, c, d = 0, 10, 25  # center
center = (b, c, d)
P = np.matrix([[1, 0, -b / d, 0], [0, 1, -c / d, 0], [0, 0, 0, 0], [0, 0, -1 / d, 1]])
PD = P * D
PD = PD / PD[3, :]
PRD = P * RD
PRD = PRD / PRD[3, :]

f4, ax4 = plt.subplots(1, 2)
for i in range(16):
    for j in range(i + 1):
        if C[i, j] == 1:
            ax4[0].plot([PD[0, i], PD[0, j]], [PD[1, i], PD[1, j]], "g")
            ax4[1].plot([PRD[0, i], PRD[0, j]], [PRD[1, i], PRD[1, j]], "r")
ax4[0].axis("off")
ax4[1].axis("off")
ax4[0].set_title("Center at " + str(center))
ax4[1].set_title("Rotated 45° about the z axis")
plt.savefig("Toyota_Normal_and_Rotated_45z.png")

A = np.matrix([[1.5, 0,  0, 0],
               [0, 1.5, 0, 0],
               [0, 0, 1.5, 0],
               [0, 0, 0, 1]])
AD = A * D
b, c, d = 0, 10, 25  # center
center = (b, c, d)
P = np.matrix([[1, 0, -b / d, 0], [0, 1, -c / d, 0], [0, 0, 0, 0], [0, 0, -1 / d, 1]])
PD = P * D
PD = PD / PD[3, :]
PAD = P * AD
PAD = PAD / PAD[3, :]

f5, ax5 = plt.subplots(1, 2)
for i in range(16):
    for j in range(i + 1):
        if C[i, j] == 1:
            ax5[0].plot([PD[0, i], PD[0, j]], [PD[1, i], PD[1, j]], "g")
            ax5[1].plot([PAD[0, i], PAD[0, j]], [PAD[1, i], PAD[1, j]], "r")
ax5[0].axis("off")
ax5[1].axis("off")
ax5[0].set_title("Center at " + str(center))
ax5[1].set_title("Zoomed 150%")
plt.savefig("Toyota_Normal_and_Zoomed.png")
