'''distribution plots '''
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

'''distribution plots are of 3 types-
1.rugplot 
2.histogram
3.kde plot '''

df=pd.read_csv(r"C:\Users\soham\Downloads\dmofficesales.csv")
#print(df.info())

'''rugplot'''
#sns.rugplot(x='salary',data=df,height=0.5)

#we can edit the height by using height= parameter

'''displot and histplot
mostly we only use displot instead of histplot , both essentially show the same thing 
but displot is more advanced and can show all 3 graphs at once '''

sns.set(style='ticks')
#there are different styles like - whitegrid , darkgrid , ticks , white , dark
# we can change the style of the graph using set function

# sns.displot(data=df,x='salary',bins=100,kde=True)

#we can change the bin size or the no of portions x axis is divided into by using the parameter bins=
#we mostly change the binsize for more precision
#as seaborn is built on top of matplotlib, we can use matplotlib functions alongside seaborn
#we can use color parameter to change the color of graph , edgecolor to color the edges 
#we can use linewidth , linestyle
# we normally dont use ls , lw with these 

'''kdeplot
The KDE plot maps an estimate of a probability density function of a random variable.
Kernel density estimation is a fundamental data smoothing problem where 
inferences about the population are made, based on a finite data sample.'''

np.random.seed(0)
sample_ages=np.random.randint(0,100,200)
sample_ages=pd.DataFrame(data=sample_ages,columns=['ages'])
print(sample_ages)

sns.kdeplot(data=sample_ages,x='ages',clip=(0,100),bw_adjust=0.01)

#we can use clip parameter to clip the kde graph
#we can use bw_adjust parameter to adjust the bandwidth

plt.show()
print(df['salary'].dtype)
