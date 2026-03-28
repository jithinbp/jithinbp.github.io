import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

def dsine_erf(p,y,x):
	return y - p[0] * np.sin(2*np.pi*p[1]*x+p[2]) * np.exp(-p[4]*x) + p[3]

def dsine_eval(x,p):
	return     p[0] * np.sin(2*np.pi*p[1]*x+p[2]) * np.exp(-p[4]*x) - p[3]

def fit_dsine(xa, ya, freq = 1000):  # guess frequency is 1000 Hz
	amp = (max(ya)-min(ya))/2
	par = [amp, freq*0.001, 0.0, 0.0, 0.1] # Amp, freq, phase , offset, decay constant
	plsq = leastsq(dsine_erf, par,args=(ya,xa))
	if plsq[1] > 4:
		return None
	yfit = dsine_eval(xa, plsq[0])
	return yfit,plsq[0]
	
	
x = np.loadtxt('RLCTransient.csv', delimiter=',', skiprows=1)
t, v = x.T
plt.plot(t,v)

res = fit_dsine(t,v, 1000)   # analysis
if res != None:
	par = res[1]
	fdata = res[0]
	freq = par[1]
	damping = par[4] / (2 * np.pi * par[1]) # unitless damping factor
	print ('Resonant Frequency = %5.0f Hz Damping Factor = %5.3f'%(freq, damping))
	plt.plot(t, fdata)
else:
	print('Fitting failed')

plt.show()

