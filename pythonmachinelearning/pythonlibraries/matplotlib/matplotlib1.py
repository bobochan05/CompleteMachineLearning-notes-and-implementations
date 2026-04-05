'''using matplotlib for graphs and visualisations '''
from matplotlib import pyplot as plt
import numpy as np 

x=np.arange(0,11)
print(x)
y=x*2
'''plt.plot(x,y)
plt.title("first graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.xlim(0) 
plt.ylim(0)
plt.show() will display the figure 
plt.savefig('first_plot.jpg') will save the figure'''

#plt.figure() creates a blank canvas where we can add our own axes and plot graphs
fig = plt.figure()
axes=fig.add_axes([0.1, 0.1, 1, 1]) # [left, bottom, width, height]
axes.plot(x, y) #plotting on those set of axes
plt.show()


