import matplotlib.pyplot as plt, numpy as np
import eyes17.eyemath17 as em   # eyemath17.py calls the scipy curve fitting routines

v,i = np.loadtxt('diode-iv.csv', delimiter=",", dtype=float).T
plt.plot(v, i, 'x')

fit = em.fit_exp(v,i)			# Fit the data using the exponential function
if fit != None:					# Fitting successful
	plt.plot(v, fit[0])
	a = fit[1]          	# parameters Io = a[0], q/nkT = a[1] and DC Offset = a[2]
	n = 2.0 					# ~1 for Silicon, and ~2 for Germanium 
	T = 300					# room temperature in Kelvin
	q = 1.6e-19     		# Charge of electron
	k = q/(n*T*a[1])
	Io = a[0]*1e-3			# mA to Ampere
	result = 'Analysis results: Io = %5.2e A\nBoltzmann Constant = %5.2e '%(Io,k)
	Io = print(result, Io, k)
else:
	result = 'Curve fitting failed'

plt.title('PN Junction V-I graph.\n'+result)
plt.show()

