import matplotlib.pyplot as plt, numpy as np


v,i = np.loadtxt('npn-ce-transfer.csv', delimiter=",", dtype=float).T
plt.plot(v, i, 'x')


# Do a least square fit to find out the slope Ic/Ib

vbar = np.mean(v)
ibar = np.mean(i)

b = sum(i*(v-vbar)) / sum(v*(v-vbar))
a = ibar - vbar * b

plt.xlabel('Ib')
plt.ylabel('Ic')
plt.title('Transistor with Ic/Ib = %5.0f'%b)
print('Beta = ',b)

plt.show() 
