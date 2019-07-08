%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

#plot a sin curve from 0 to 2pi

t = np.linspace(0,2*np.pi,100)
plt.plot(t,np.sin(t),'m', label = 'Sine Curve')
plt.title('Plot of $\sin{x}$')
plt.xlabel('t (s)')
plt.ylabel('$y(t)$')
plt.legend()
plt.grid()
plt.text(4,0.25,'This is a \nSine Curve!', fontsize = 16)
plt.text(1,-0.25,'Wow!', fontsize = 16)
plt.show()
