'''grid plots '''
import numpy as np 
import pandas as pd 
import seaborn as sns 
from matplotlib import pyplot as plt

df=pd.read_csv(r"C:\Users\soham\Downloads\StudentsPerformance.csv")
print(df)

#catplot()
sns.catplot(data=df, x='gender' , y='math score' , kind='bar',row='lunch', col='test preparation course',hue='parental level of education')

#PairGrid()
p=sns.PairGrid(df)
p.map_upper(sns.histplot)
p.map_lower(sns.scatterplot)
p.map_diag(sns.kdeplot)


plt.show()

