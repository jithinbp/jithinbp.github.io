import matplotlib.pyplot as plt, numpy as np
import eyes17.eyes, time

p = eyes17.eyes.open()

Rc = 1					# 1 kOhm, using kOhm gives current in mA
Rb = 100
p.set_pv2(1)			# Set the base current = (PV2-A2)/100k
va = [0]
ia = [0]

f = open('npn-ce-output.csv','w')		# file to write data

v = 0.1
while v < 5:
	p.set_pv1(v)
	time.sleep(0.1)
	vc = p.get_voltage('A1')
	ic = (v-vc)/Rc
	va.append(vc)
	ia.append(ic)
	s = '%5.3f,\t%5.3f'%(vc,ic)
	print(s)
	f.write(s+'\n')
	v += 0.2
	
	plt.clf()				# clear plot
	plt.plot(va,ia, 'x')	# draw new plot
	plt.pause(.01)			# pause is required

plt.xlabel('Volatge (V)')
plt.ylabel('Current (mA)')
plt.title('Transistor Vc-Ic curve')
plt.show() 
