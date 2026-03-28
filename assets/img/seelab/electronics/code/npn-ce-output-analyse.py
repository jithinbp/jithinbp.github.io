import matplotlib.pyplot as plt, numpy as np


v,i = np.loadtxt('npn-ce-output.csv', delimiter=",", dtype=float).T

v = v[10:]   # take ony the linear part for finding the output resistance
i = i[10:]
plt.plot(i, v, 'x')

x = i
data = v

# Do a least square fit to find out the slope dy/dx
xbar = np.mean(x)
ybar = np.mean(data)
b = sum(data*(x-xbar)) / sum(x*(x-xbar))
a = ybar - xbar * b
print(a,b)

y = a + b * x
plt.plot(x,y)

plt.xlabel('Current')
plt.ylabel('Voltage')
plt.title('dV/dI : Dynamic Output Impedance = %6.1f kOhm'%b)
plt.show() 
