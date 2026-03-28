import matplotlib.pyplot as plt, numpy as np
import eyes17.eyemath17 as em   # eyemath17.py calls the scipy curve fitting routines


res = np.loadtxt('cap-ac.csv', delimiter = ',').T	# transpose for clolumn-wise data

t = res[0]
vc = res[1]
ic = res[2] / 1000

# Analyse by fitting both graphs using sinusoid. V = Vo sin (2 pi f t + theta) + C
# If curve fitting fails, program will exit

fvc = em.fit_sine(t, vc)			# returns fitted dataset and the parameters
fic = em.fit_sine(t, ic)

par1 = fvc[1]
par2 = fic[1]

freq = par1[1] * 1000   # time is in mS
dphi = (par2[2]-par1[2]) * 180 / np.pi

zc = par1[0]/ par2[0]		# Amplitude of voltage / amplitude of current (I in mA)

C = 1 / (2 * np.pi * freq * zc) * 1e6  # Farads to micro Farads

print ('Frequency = %4f Hz. Phase diff. = %5.1f Deg. C = %5.3f uF'%(freq, dphi, C))

plt.plot(t, fvc[0])
plt.plot(t, fic[0])
plt.show()
