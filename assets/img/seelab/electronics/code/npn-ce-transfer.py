import matplotlib.pyplot as plt

import eyes17.eyes
p = eyes17.eyes.open()

f = open('npn-ce-transfer.csv','w')		# file to write data

R = 1  # in kOhms, gives current in mA

Vcc = 5
p.set_pv1(Vcc)

x = []
y = []
vbr = 0.2
while vbr < 2:
	p.set_pv2(vbr)
	vb = p.get_voltage('A2')
	ib = (vbr-vb)/100			# 100k resistor
	vc = p.get_voltage('A1')
	ic = (Vcc-vc)/R
	x.append(ib)
	y.append(ic)
	s = '%5.3f,\t%5.3f'%(ib,ic)
	print(s)
	f.write(s+'\n')
	vbr += 0.1

plt.plot(x,y)
plt.show() 
