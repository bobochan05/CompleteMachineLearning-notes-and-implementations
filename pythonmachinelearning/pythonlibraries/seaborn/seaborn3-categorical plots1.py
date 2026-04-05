'''categorical plots 
Often we have categorical data, meaning the data is in distinct groupings,
such as Countries or Companies. There is no country value "between" USA and France 
and there is no company value "between" Google and Apple, 
unlike continuous data where we know values can exist between data points, such as age or price.'''

import numpy as np
import pandas as pd 
import seaborn as sns
from matplotlib import pyplot as plt
df=pd.read_csv(r"C:\Users\soham\Downloads\dmofficesales.csv")
print(df.head())

'''countplot()- this is the visualization method of calling value_counts() function '''

plt.figure(figsize=(9 ,5),dpi=100)
plt.title('count of employees in each division')
plt.ylabel('no of counts')
sns.countplot(x='division',data=df,palette='Set2', hue='level of education')
#we can pass hue paramater to see more info 

'''barplot()-'''

plt.figure(figsize=(15 ,5))
plt.title('average salary of employees in each division')
plt.ylabel('average salary')
sns.barplot(x='division',y='salary',data=df,palette='Set2',hue='level of education') 
plt.legend(loc=(1.05,0.5))

plt.show()
