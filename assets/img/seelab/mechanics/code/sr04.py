import eyes17.eyes, time
p = eyes17.eyes.open()

ta = []
da = []

strt = time.time()
f = open('sr04.csv', 'w')		# file to save the results

for k in range(100):
	tm, dist = p.sr04_distance_time()
	res = '%f,\t%f'%(tm-strt, dist)
	f.write(res+'\n')
	print(res)
	time.sleep(0.05)



