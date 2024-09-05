import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, ion, show

matplotlib.use('tkagg')

ion()
x = np.linspace(0, 2 * math.pi, 200)
plt.plot(x, np.sin(x))
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("sin(x) vs x")
show()
plt.savefig('sine.png')
