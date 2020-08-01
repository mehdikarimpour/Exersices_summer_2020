import numpy as np
import matplotlib.pyplot as plt
plt.figure()
x=np.linspace(0,10,100)
y=(1/(np.e**(x/10)))*np.sin(np.pi*x)
#plt.plot(x,y)
plt.xlabel('mehvare x')
plt.ylabel('mehvare y')

plt.figure()
x=np.linspace(0,10,100)
y=x*(1/(np.e**(x/3)))
#plt.plot(x,y)
plt.xlabel('mehvare x')
plt.ylabel('mehvare y')


plt.figure()
r0=1.2
teta=np.linspace(0,2*np.pi,360)
r=1+np.cos(teta)
x=r*np.cos(teta)
y=r*np.sin(teta)
plt.plot(x,y)
plt.show()
