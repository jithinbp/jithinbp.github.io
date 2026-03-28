'''
Connections
         R2             R1
PV1----/\/\/\----A1---/\/\/\-----GND
                              1K        
R2 is the resistor to be measured, Use values from 100 Ohms to 10 kOhms.
'''

import eyes17.eyes, time
p = eyes17.eyes.open()

Vp = 2.0
p.set_pv1(Vp)
time.sleep(.2)

Va1 = p.get_voltage('A1')
R1 = 1000

I = Va1 / R1 	# Current through R1 = Va/R. 
#Same current passes through R2 (igroring the 1Meg input impedance of A1)

R2 = (Vp-Va1) / I

print ('Voltage at PV1 =  %5.3f V.  Voltage at A1 = %5.3f V.\nCurrent = %7.6f A'%(Vp,Va1,I) )

print ('Voltage across R2 = %5.3f V. Value of R2 = %5.0f Ohm'%(Vp-Va1, R2))
