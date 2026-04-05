import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("C:\\Users\\soham\\Downloads\\Advertising.csv")
print(df.head())
df['Total Spend']=df['TV']+df['radio']+df['newspaper']
X=df['Total Spend']
y=df['sales']
sns.scatterplot(data=df,x='Total Spend',y='sales')
sns.regplot(data=df , x='Total Spend', y='sales')
# plt.show()

# (np.polyfit) fits a least squares polynomial to data
print(np.polyfit(X,y,deg=1))
potential_spend=np.linspace(0,600,100)
potential_sales=0.04868788*potential_spend + 4.24302822
plt.plot(potential_spend,potential_sales, color='red')
plt.show()
