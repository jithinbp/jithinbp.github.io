'''
Connections for RL transient
--|--OD1 --1K--|--Inductor---GND
  A2           A1     
'''

import matplotlib.pyplot as plt, time
import eyes17.eyes, eyes17.eyemath17 as em

p = eyes17.eyes.open()

p.set_state(OD1=0)		# OD1 to LOW
time.sleep(.5)
t,v = p.capture_action('A1', 500, 1,'SET_HIGH')

t = t[2:]		# take the exponetial part only
v = v[2:]

plt.plot(t,v)

Rext = 1000
fa = em.fit_exp(t,v)
if fa != None:
	p.set_state(OD1=1)				# Do some DC work to find the resistance of the Inductor
	time.sleep(.5)
	Vind = p.get_voltage('A1')     	# voltage across the Inductor
	Vout = p.get_voltage('A2')		# voltage at OD1, if A2 s connected there
	if Vout < 4.0:					# Means user has NOT connected OD1 to A2
		Vout = 5.0
	i = (Vout - Vind)/Rext
	Rind = Vind/i	
	Rtotal = Rind + Rext
	print ('DC Voltage applied = %5.3f V'%Vout)
	print ('Voltage across Inductor = %5.3f V (Assuming 1k external R)'%Vind)
	print ('Resistance of the inductor = %5.3f Ohms'%Rind)
	
	rbl = abs(fa[1][1])				# R/L value extracted by curve fitting, t is in milliseconds
	print ('Extracted R/L = %5.3f. Inductance = %5.1f mH'%(rbl, Rtotal/rbl))	
	plt.plot(t,fa[0])
plt.show()

