%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

#plot exponential curve from 0 to 2pi

t = np.linspace(0,2*np.pi,100)
plt.plot(t,np.exp(t),'m', label = 'Exponential Curve')
plt.title('Plot of $e^x$')
plt.xlabel('t (s)')
plt.ylabel('$y(t)$')
plt.legend()
plt.grid()
plt.text(2.5,0.25,'This is a \nExponential Curve!', fontsize = 16)
plt.text(1,-0.5,'Cool!', fontsize = 16)
plt.show()
