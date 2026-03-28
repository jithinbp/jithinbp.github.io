import eyes17.eyes, time, numpy as np
p = eyes17.eyes.open()
import matplotlib.pyplot as plt

R = 1  # 1k resistor for current measurement
NP = 500
TG = 40
fr = 150
p.set_sine(fr)
time.sleep(.2)

f = open('cap-ac.csv', 'w')		# file to save the results

p.configure_trigger(1, 'A2', 0)
data = p.capture2(NP, TG)  	# result conatins 2 time-voltage pairs
t = data[0]
ic = data[3]/R
vc = data[1] - data[3]

for k in range(NP):
	s = '%f,\t%f,\t%f\n'%(t[k], vc[k], ic[k]) 
	f.write(s + '\n')

plt.plot(data[0], vc)
plt.plot(data[0], ic)
plt.show()

