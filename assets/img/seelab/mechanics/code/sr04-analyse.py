import numpy as np
import matplotlib.pyplot as plt
import eyes17.eyemath17 as em
	
x = np.loadtxt('sr04.csv', delimiter=',', skiprows=0)
t, dist = x.T
plt.plot(t,dist)

res = em.fit_sine(t,dist)

if res != None:
	par = res[1]
	fdata = res[0]
	freq = par[1]
	print (par,'T = %5.3f Seconds'%(1/freq))
	plt.plot(t, fdata)
else:
	print('Fitting failed')

plt.show()

