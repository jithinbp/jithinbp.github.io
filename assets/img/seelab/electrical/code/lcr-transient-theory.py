import numpy as np
import matplotlib.pyplot as plt

R = 100 + 10   	# 10 Ohm coil resistance
L = 10e-3		# 10 mH
C = 0.1e-6		# 0.1 uF

B=-R/(2*L)
G=np.sqrt(1/L/C - (R/2/L)**2)
damping = (R/2) * np.sqrt(C/L)

s = 'Freq = %5.1f Hz. Damping Factor = %5.2f'%(G/(2* np.pi), damping)

t = np.linspace(0, .001, 200)     # 0 to 1 mS

v = 5* np.exp(B*t) * np.sin(G*t + np.pi/2)

plt.plot(t,v)
plt.title(s)
plt.show()

