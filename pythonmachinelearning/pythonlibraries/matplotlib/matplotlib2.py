from matplotlib import pyplot as plt
import numpy as np 
x1=np.linspace(0,10,11)
y1=x1**4
x=np.arange(0,10)
y=2*x
print(x1,y1,x,y)

fig=plt.figure(dpi=100,figsize=(12,8))#dpi is dots per inch
axes=fig.add_axes([0.1,0.1,1,1])#main axes
axes1=fig.add_axes([0.2,0.2,0.25,0.25])#inset axes
axes.plot(x1,y1)
axes1.plot(x,y)
axes.set_title("first graph")
axes.set_xlabel("X axis")
axes.set_ylabel("Y axis")
axes.set_xlim(0) 
axes.set_ylim(0)

axes1.set_title("2nd graph")
axes1.set_xlabel("X axis")
axes1.set_ylabel("Y axis")
axes1.set_xlim(0) 
axes1.set_ylim(0)

plt.show()

