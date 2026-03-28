import eyes17.eyes, time
p = eyes17.eyes.open()

#p.set_pv2(1.0)

# Set r0 by measuring the reading with melting ice
r0 = 1000			# for PT1000, supposed to be 1000 Ohm at zero degree C
A = 3.91e-3			# linear coefficient
B = -0.588e-6		# qudratic .. , this code is using only linear

TMAX = 60			# Total duration
TG = 0.5			# time gap between two readings

ta = []
ra = []

f = open('pt1000.csv', 'w')
start = time.time()
while 1:
	r = p.get_resistance()
	t = time.time() - start
	temp = ((r/r0) - 1)/A
	ta.append(t)
	ra.append(temp)
	s = '%4.2f,\t%5.1f'%(t,temp)
	f.write(s+'\n')
	print (s)
	time.sleep(TG)
	if t > TMAX:
		break
	f.flush()

import matplotlib.pyplot as plt
plt.plot(ta,ra)
plt.show()
