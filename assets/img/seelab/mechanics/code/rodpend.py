import eyes17.eyes, math
p = eyes17.eyes.open()

length = 10.0   			# 10 cm
p.set_state(SQ1 = 1)		# light the LED

for k in range(10):
	T = p.multi_r2rtime('SEN', 2)
	if T > 0:
		g = 8*math.pi**2*length/3/T**2
		print('%6.4f %5.0f'%(T, g))
	else:
		print ('timeout error')
