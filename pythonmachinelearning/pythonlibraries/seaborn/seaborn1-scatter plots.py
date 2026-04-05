'''seaborn 
Seaborn is a library for making statistical graphics in Python. 
It builds on top of matplotlib and integrates closely with pandas data structures.
For more details visit the link below'''
seaborn_info = 'https://seaborn.pydata.org/tutorial/introduction'

'''Scatter plots-'''
# a continous feature allows for a value to be between two points
# a categorial feature allows for a value to be one of a limited, fixed set of possible values

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
df=pd.read_csv(r"C:\Users\soham\Downloads\dmofficesales.csv")
print(df)
plt.figure(figsize=(12 ,6),dpi=100)
sns.scatterplot(x='salary',y='sales',data=df,hue='level of education',palette='Dark2',size='salary',alpha=0.3)
#hue is used to add a categorical column
#we can also choose colors for the scatter plot 
#we do that using palette, Choosing a palette from Matplotlib's cmap
#we can use the size option for the dots to be of that type i.e by putting
# size=salary , the higher the salary , the dots will be larger
#to make all the size large we use 's' , this increase the general size  
#to see where all the points are stacked we can use the alpha parameter 
#alpha=1 means full opacity , alpha =0 means 0 opacity so we must choose something in between
# we can use the style parameter to see them in diff shapes 
#mostly people use style and hue together

cmap_link='https://matplotlib.org/stable/users/explain/colors/colormaps.html'
plt.show() # this has to used everytime to show the graph as seaborn is based of matplotlib




