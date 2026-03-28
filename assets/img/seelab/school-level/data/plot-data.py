import numpy as np
import matplotlib.pyplot as plt

x = np.loadtxt('sr1.csv', delimiter=',', skiprows=1)
t, d = x.T
t = t-2.612      # make start time zero
d = d - 4.7      # and starting distance zero
plt.plot(t,d, 'x-', label='Expt')
plt.plot(t, 0.5 * 980 * t**2, 'o', label='theory')
plt.xlabel('Time')
plt.ylabel('Distance')
plt.legend()
plt.show()

