'''subplots'''
import numpy as np
from matplotlib import pyplot as plt

a=np.linspace(0,10,11)
b=a**4

x=np.arange(0,10)
y=2*x

fig,axs=plt.subplots(1,2)
axs[0].plot(a,b)
axs[1].plot(x,y)

fig2,axs2=plt.subplots(2,2)
axs2[0,0].plot(a,b)
axs2[0,1].plot(x,y)
axs2[1,0].plot(x,y)
axs2[1,1].plot(a,b)

plt.tight_layout() # this will space out the subplots

fig.subplots_adjust(left=None,
    bottom=None,
    right=None,
    top=None,
    wspace=0.9,
    hspace=0.1,)

fig2.subplots_adjust(left=None,
    bottom=None,
    right=None,
    top=None,
    wspace=0.9,
    hspace=0.1,)

plt.show()