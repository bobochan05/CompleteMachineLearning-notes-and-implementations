'''styling -legends '''

import numpy as np
from matplotlib import pyplot as plt
x = np.arange(0,10,0.1)
# Example of plotting with legends
fig = plt.figure(dpi=100,figsize=(10,4)) 

ax = fig.add_axes([0.1,0.1,1,1])
ax.set_xlim([0, 10])
ax.set_ylim([0, 200])

ax.plot(x, x**2, color='green',label="x**2",lw=0.5,ls='--',marker='o')
ax.plot(x, x**3,color='darkblue', label="x**3",lw=1,ls='-.',marker='o')
#the loc argument helps programmer to place the legend
ax.plot(x, x**4, color='lightblue',label="x**4",lw=0.5,ls=':',marker='o')
# we can use lw to increase the width of the line
# we can use ls to change the line style
# we can use marker to marks the points 
# we can use ms to change the size of marker
ax.legend(loc='lower left')

plt.show()