'''comparison plots '''

import numpy as np 
import pandas as pd 
import seaborn as sns 
from matplotlib import pyplot as plt

df=pd.read_csv(r"C:\Users\soham\Downloads\StudentsPerformance.csv")
print(df)

'''jointplot()'''
sns.jointplot(data=df, x="math score", y="reading score", palette="Set2",kind='hex')
#we can use kind to change the type of plot
#kind can be "scatter", "kde", "hist", "hex"
#sns.jointplot(data=df, x="math score", y="reading score", hue="gender", palette="Set2", kind="kde")

'''pairplot()'''
sns.pairplot(data=df, hue="gender", palette="Set2")

plt.show()