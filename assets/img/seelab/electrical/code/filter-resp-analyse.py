import numpy as np
import matplotlib.pyplot as plt
import eyes17.eyemath17 as em

x = np.loadtxt('filter-resp.csv', delimiter=',', skiprows=0)
print(x)
f,ain,aout = x.T
gain = aout/ain

plt.plot(f, gain, 'x')

fit = em.fit_gauss(f,gain)
print (fit[1])
plt.plot(f,fit[0])
plt.show()
