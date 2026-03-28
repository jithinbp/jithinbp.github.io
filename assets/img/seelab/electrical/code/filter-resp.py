import eyes17.eyes, time
p = eyes17.eyes.open()

FMIN = 200
FMAX = 1000
STEP = 25

p.select_range('A1',4)
p.select_range('A2',4)
p.configure_trigger(0,'A2',0.0)

f = open('filter-resp.csv','w')		# file to write data

for freq in range(FMIN, FMAX, STEP):
	fr = p.set_sine(freq)
	time.sleep(0.5)
	res = p.capture2(1000, 10)   # captures A1 and A2
	Aout  = (res[1].max() - res[1].min()) / 2
	Ain = (res[3].max() - res[3].min() ) / 2

	s = '%4.0f,\t%5.2f,\t%5.2f'%(fr, Ain, Aout)
	print (s)
	f.write(s+'\n')
	
