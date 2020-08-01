import numpy as np
#import scopy.linalg as la
import matplotlib.pyplot as plt
x=5
p1=pow(x,2)
p2=pow(x,3)
teta=int(input("enter a value:"))
meshPoints=np.linspace(-1,1,500)
sin=np.sin(teta)
b1=np.sin(meshPoints)
plt.plot(meshPoints,np.sin(2*(np.pi)*meshPoints))
