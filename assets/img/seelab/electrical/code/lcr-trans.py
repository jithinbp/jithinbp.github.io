import eyes17.eyes, time, numpy as np

p = eyes17.eyes.open()

NP = 500
TG = 2

p.select_range('A1',8)

p.set_state(OD1=1)		# OD1 to HIGH
time.sleep(.1)
res = np.empty((2,NP))
res[0], res[1] = p.capture_action('A1', NP, TG, 'SET_LOW')

np.savetxt('lcr.csv', res.T, delimiter = ',', header = 'Time, Voltage')	# transpose to write as 2 columns

import matplotlib.pyplot as plt
plt.plot(res[0], res[1])
plt.show()
