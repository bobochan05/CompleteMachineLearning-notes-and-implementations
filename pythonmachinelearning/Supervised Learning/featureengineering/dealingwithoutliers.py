'''
feature engineering refers to cleaning the data before using it for analysis or modeling.
This process may include handling missing values, encoding categorical variables, normalizing numerical features
and creating new features from existing ones to improve model performance.
'''


'''
In statistics, an outlier is a data point that differs significantly from other observations.
An outlier may be due to variability in the measurement or it may indicate experimental error
the latter are sometimes excluded from the data set. An outlier can cause serious problems in statistical analyses.

Remember that even if a data point is an outlier, its still a data point! Carefully consider your data, its sources
and your goals whenver deciding to remove an outlier. Each case is different!
'''

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

#function to generate random data with outliers
def create_ages(mu=50,sigma=13,num_samples=100,seed=42):
    # Set a random seed in the same cell as the random call to get the same values as us
    # We set seed to 42 (42 is an arbitrary choice from Hitchhiker's Guide to the Galaxy)
    np.random.seed(seed)
    sample_ages = np.random.normal(loc=mu,scale=sigma,size=num_samples)
    sample_ages = np.round(sample_ages,decimals=0)
    return sample_ages

#calling the function to create ages
ages = create_ages()
#print("ages:",ages)
#sns.boxplot(ages)
age=pd.Series(ages)
print(age.describe())
#calculating IQR to identify outliers
q1=age.quantile(0.25)
q3=age.quantile(0.75)
iqr=q3 - q1
print("IQR:",iqr)
lower_bound=q1 - 1.5*iqr
upper_bound=q3 + 1.5*iqr
print("lower_bound:",lower_bound)
print("upper_bound:",upper_bound)
df = pd.read_csv("C:\\Users\\soham\\Downloads\\Ames_Housing_Data.csv")
print(df.head())
#checking correlation between features
print(df.select_dtypes("number").corr()['SalePrice'].sort_values())
#visualizing SalePrice distribution with overall quality
#sns.scatterplot(x='Overall Qual',y='SalePrice',data=df)
#sns.scatterplot(x='Gr Liv Area',y='SalePrice',data=df)

'''Removing outliers based on domain knowledge
In this case we know that houses with more than 4000 sqft of living area are rare and expensive
but here we are seeing that the houses with great living area and overall qual are not selling for high prices
so we can remove those outliers. They are being sold at a bargain price for some unknown reason.
'''
df_no_outliers = df[(df['Gr Liv Area'] < 5000) & (df['SalePrice'] > 200000)]
sns.scatterplot(x='Gr Liv Area',y='SalePrice',data=df_no_outliers)
plt.show()

