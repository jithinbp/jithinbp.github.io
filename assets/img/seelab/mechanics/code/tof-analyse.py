import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def gaussian(x, a, mean, sigma):		# The Gaussian function
	return a * np.exp(-((x - mean)**2 / (2 * sigma**2)))

S = 0.30   						# 30 cm height
NBINS = 10
tof = np.loadtxt("tof.csv")		# Expect a single column data
npoints = len(tof)
if npoints >= 2*NBINS:
	print('Loaded %d items'%npoints)
else:
	print('Insufficient data')

g = 2*S/tof**2		# Acceleration due to gravity
yh,xh = np.histogram(g, bins=NBINS)		

# histogram() function returns the NBINS+1 edges of the histogram,
# Calculate the NBINS midpoints
for k in range(NBINS):
	xh[k] = (xh[k]+xh[k+1])/2
for k in range(NBINS):
	xh[k] = (xh[k]+xh[k+1])/2
	
xhmid = xh[:-1]		# truncate the last point, makes it NBINS points

# Get the parameter guess values, for the curve_fit function.
amp = yh.max()
mean = g.mean()
sigma = g[1]-g[0]
pars, fdata = curve_fit(gaussian, xhmid, yh, [amp, mean, sigma])
print('Amplitude %f | Mean %f | Sigma %f'%(pars[0],pars[1],pars[2]))

ss = r'$g = %7.3f\pm%7.5f$'%(pars[1],abs(pars[2]))	# using LaTex 
plt.title(ss)

plt.plot(xhmid, yh, 'x-', label='Expt')

#xh = np.linspace(xh[0], xh[-1], 100)   #uncomment to get a smoother fitted graph

plt.plot(xh, gaussian(xh, *pars), label='Fitted')
plt.legend()
plt.show()
