'''boxplots and other types of categorical plots'''

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df=pd.read_csv(r"C:\Users\soham\Downloads\StudentsPerformance.csv")
print(df) 

'''boxplot()'''
#sns.boxplot(data=df , x="gender", y="math score" , palette='Set2', hue='test preparation course')

'''violinplot()'''
#sns.violinplot(data=df ,x="gender", y="math score" , palette='Set2', hue='test preparation course')
#we can set inner=none to remove the inner boxplot
#we can set inner=quartile to show the quartiles
#we can set inner=stick to show the stick

'''swarmplot()'''
sns.swarmplot(data=df , x="gender", y="math score" , palette='Set2', hue='test preparation course')
#sometimes the dots are too large to fit in the axes thus we can use the size parameter to change its size
plt.figure(figsize=(12,6),dpi=100)
#sns.swarmplot(data=df , y='math score',x='gender', size=4, hue='test preparation course' , palette='Set2',dodge=True)
#we can use the dodge parameter to separate the points

'''boxenplot()'''
sns.boxenplot(data=df , x="gender", y="math score" , palette='Set2', hue='test preparation course')


plt.show()



