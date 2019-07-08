%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

#plot a cos curve from 0 to 2pi

t = np.linspace(0,2*np.pi,100)
plt.plot(t,t,'m', label = 'Cosine Curve')
plt.title('Plot of $\cos{x}$')
plt.xlabel('t (s)')
plt.ylabel('$y(t)$')
plt.legend()
plt.grid()
plt.text(2.5,0.25,'This is a \nCosine Curve!', fontsize = 16)
plt.text(1,-0.5,'Cool!', fontsize = 16)
plt.show()
