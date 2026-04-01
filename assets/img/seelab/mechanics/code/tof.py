import eyes17.eyes
p = eyes17.eyes.open()
print(p.get_version())

S = 0.30    # height
f = open('tof.csv', 'w')
for k in range(100):
	p.set_state(OD1 =0)	# The relay used is energized when control voltage is LOW.
	input('Attach the ball and press the Enter key')
	res = p.set2ftime('OD1', 'SEN')		# SEN goes LOW when the ball hits the sensor.
	if res < 0:
		print ('Timeout Error')
		continue
	res -= 0.003  # 3 mS delay in releasing the ball
	ss = '%f'%res
	f.write(ss+'\n')
	f.flush()
	print(k,res,2*S/res**2)


