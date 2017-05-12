import math
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-5,5,100)

y=np.log(x)
y1=np.log10(x)
y2=-y
y3=-y1
y4=np.tan(x)
plt.plot(x,y)
plt.axhline(y=0,color='r')
plt.axvline(x=0,color='r')
plt.plot(x,y1,color='black',ls='--')
plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y4)
plt.ylim(-5,5)
plt.show()