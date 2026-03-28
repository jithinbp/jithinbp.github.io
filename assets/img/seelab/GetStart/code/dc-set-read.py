# Connect PV1 to A1.
import eyes17.eyes, time
p = eyes17.eyes.open()

p.set_pv1(2.0)
time.sleep(.2)

print ('Voltage at A1 = ', p.get_voltage('A1'))

print ('Capaciance at IN1 = ',p.get_capacitance())

print ('Resistance at SEN = ',p.get_resistance())
