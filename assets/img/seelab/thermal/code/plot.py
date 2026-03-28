import numpy as np
import matplotlib.pyplot as plt

x,y = np.loadtxt("pt1000.csv", delimiter=',').T

plt.plot(x,y)
plt.show()
