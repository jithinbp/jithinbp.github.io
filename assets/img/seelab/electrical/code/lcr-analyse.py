import numpy as np
import matplotlib.pyplot as plt
import eyes17.eyemath17 as em
	
x = np.loadtxt('lcr.csv', delimiter=',', skiprows=0)
t, v = x.T
plt.plot(t,v, 'x')

res = em.fit_dsine(t,v)

if res != None:
	par = res[1]
	fdata = res[0]
	freq = par[1]
	damping = par[4] / (2 * np.pi * par[1]) # unitless damping factor
	s ='Resonant Frequency = %5.3f kHz\nDamping Factor = %5.3f'%(freq, damping)
	plt.plot(t, fdata)
	plt.title(s)
else:
	plt.title('Fitting of data failed')

plt.show()

