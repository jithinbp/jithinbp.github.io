---
layout: project
title: 'Software PID controller'
date: 20 Oct 2011
image: /assets/img/mastersacad/pid-can2.jpg
caption: Uses a sourcemeter, and a voltmeter to control the temperature of a PCB sealed inside a can and immersed in liquid nitrogen.
description: >
    A diode based temperature sensor is used for measuring, and a voltage regulator was repurposed (misused) as a heating element .  A python script converts the voltage values read from the sensor into temperature via a fitting function based on a look up table provided by the manufacturer. It then decides the the amount of current to send to the heater based on the standard PID equation.
accent_color: '#4fb1ba'
accent_image:
  background: 'url(/assets/img/bg_elec.jpg)'
  overlay:    true
---

* this list will be replaced by the toc
{:toc .large-only}

## Results

Stability of around 25mK was achieved

![Full-width image](/assets/img/mastersacad/awesomeness.png){:.lead width="800" height="100" loading="lazy"}
Final stability of the PID controller
{:.figcaption}


## Source Code

```python
import Gpib,time,string				#python GPIB wrapper used
from Tkinter import *				#used for graphics
#import eyeplot2 as eyeplot, eyemath,sys,math
import pygrace

#y = 512.93 - 424.79 * x + 60.2 * x^2 - 60.75 * x^3

WIDTH  = 800   # width of drawing canvas
HEIGHT = 400   # height 
#pid constants

c1=500 #500
c2=200.0
c3=-400.0 #-400

integral=1	#updated later
derivative=1 #updated later
pid_mA=300
droop=0
temp='?'

def temperature(x):				#function returns corresponding temperature
	return 512.93 - 424.79 * x + 60.2 * x*x - 60.75 * x*x*x  #using fitted data equation
	
b=Gpib.Gpib('voltmeter')			#create instances to instruments
a=Gpib.Gpib('sourcemeter')

def readval():					#function to measure resistance
	b.clear()
	b.write(":DATA?")			#query data
	data=b.read(28)				#read data
	return data

pg = pygrace.grace()

a.clear()

a.write(":OUTP OFF")				#turn off output

a.write(":SOUR:FUNC CURR")			#set output to constant current mode
a.write(":SOUR:CURR:MODE FIX")
a.write(":SOUR:CURR:RANG 1")			#set 1A current max

start=time.time()
x=[]
y=[]
set_temp=93.0
fi=open('pid100ma.txt','wt')			#data file
def initialize():
	global start
	start = time.time()

def xmgrace():
	global x,y,set_temp,pg,temp,droop
	pg.clear()
	pg.plot(x,y)
	pg.xlabel('Time')
	pg.ylabel('Temperature')
	pg.title('set to '+str(set_temp)+'K, now at %.4f'%(temp)+'droop=%.6f'%(droop) )
	
def record():
	global set_temp,x,y,integral,derivative,temp,droop,overshoot
	root.after(500,record)			#automatically repeat function after 500ms
	if not rec.get():			#check status of checkbutton
		return				#return if false
	#x=string.split(val,',')
	#volt=string.atof(x[0])
	volt=string.atof(readval())		#ASCII to float conversion
	temp=temperature(volt)
	dt=time.time()-start
	dtemp=set_temp+droop-temp
	difference=set_temp+droop-temp
	pid_mA=300
	if len(x)>30:
		sd=0
		thirty_points=y[-30:]
		for r in thirty_points:
			sd+=(abs(r-thirty_points[0]))/30.0
		print 'deviation',sd
		if sd<0.02: #apply droop correction
			if(y[-1]<set_temp ):
				if(overshoot==True):
					droop+=(set_temp-y[-1])/10.0
					overshoot=False
					msgwin.config(col='green')
					
			elif(y[-1]>set_temp):
				droop-=	0.1
				msgwin.config(col='red')
			print 'droop offset = ',droop
	a.clear()
	if len(x)>8:
		last_five_points=y[-5:]
		time_taken=x[-1]-x[-5]
		integral=0
		derivative=0
		for r in last_five_points:
			integral+=(r-last_five_points[0])/time_taken

		derivative=(last_five_points[4]-last_five_points[0])
		print difference*c1,integral*c2,derivative*c3,'heat out=',\
		difference*c1+integral*c2+derivative*c3
		pid_mA=c1*difference+c2*integral+c3*derivative

	if(pid_mA>800):pid_mA=800
	if(pid_mA<0):pid_mA=1
	a.clear()
	q=":SOUR:CURR:LEV "+str(int(pid_mA))+"E-3"
	print q
	a.write(q)
	a.clear()
	if(difference<-1):
		a.write(":OUTP OFF")
	else:
		a.write(":OUTP ON")
	x.append(dt)
	y.append(temp)
	if(temp>set_temp and y[-3]<set_temp):
		overshoot=True
	xmgrace()
	fi.write("%s %s\n"%(dt,temp))#write to file
		
root=Tk()									#create a window
root.lift()
#g = eyeplot.graph(root, width=WIDTH, height=HEIGHT)	# make plot objects using draw.disp

rec=IntVar()
c = Checkbutton(root, text="RECORD DATA", bd=5 ,cursor='spider',relief='raised' ,\
variable=rec,command=initialize )
c.pack(side = LEFT, anchor = N)				#disply a button
msgwin = Label(root,text='droop correction', fg = 'blue')
msgwin.pack(side=BOTTOM, anchor = S, fill=BOTH, expand=1)

root.title('temperature')
root.after(100,record)
root.mainloop()								#loop infinitely
```

