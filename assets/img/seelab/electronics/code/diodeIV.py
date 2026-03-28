import matplotlib.pyplot as plt, numpy as np
import eyes17.eyes, time

p = eyes17.eyes.open()
p.set_pv1(0)
R = 1		# 1 kOhm, using kOhm gives current in mA
va = [0]
ia = [0]

f = open('diode-iv.csv','w')		# file to write data

v = 0.2
while v < 5:
	p.set_pv1(v)
	time.sleep(0.1)
	vd = p.get_voltage('A1')
	i = (v-vd)/R
	va.append(vd)
	ia.append(i)
	s = '%5.3f,\t%5.3f'%(vd,i)
	print(s)
	f.write(s+'\n')
	v += 0.2
	
	plt.clf()				# clear plot
	plt.plot(va,ia, 'x')	# draw new plot
	plt.pause(.01)			# pause is required

plt.xlabel('Volatge (V)')
plt.ylabel('Current (mA)')
plt.title('PN Junction V-I curve')
plt.show() 
