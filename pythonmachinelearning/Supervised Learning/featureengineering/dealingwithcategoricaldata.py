import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns   

df=pd.read_csv("C:\\Users\\soham\\Downloads\\Ames_NO_Missing_Data.csv")
print(df.head())
print(df['MS SubClass'].value_counts())
df['MS SubClass']=df['MS SubClass'].apply(str)

'''
creating dummy variables
dummy variables are binary (0 or 1) variables created to represent categories
for example, if we have a categorical variable 'Color' with categories 'Red', 'Blue', 'Green',
we can create three dummy variables: 'Color_Red', 'Color_Blue', 'Color_Green'
'''
#now dividing the dataframe into objects and numeric datatypes 
df_obj=df.select_dtypes(include=['object'])
df_num=df.select_dtypes(exclude=['object'])

#now creating a dummy variable for df_obj 
dummy_variables=pd.get_dummies(df_obj,drop_first=True)
print(dummy_variables)

# now adding the numeric dataframe and dummy variable dataframe
df_final=pd.concat([df_num ,dummy_variables],axis=1)
print(df_final.head())

'''
MS SubClass is a categorical variable (even though it looks numeric in the Ames Housing dataset).
Machine learning models cannot directly use categories, so we convert them into dummy (one-hot) variables.

dummy_variables=pd.get_dummies(df['MS SubClass'],drop_first=True)
This line creates dummy variables for each category in 'MS SubClass', dropping the first category to avoid multicollinearity.

suppose the column contains : 20, 60, 20, 120

MS_SubClass_20   MS_SubClass_60   MS_SubClass_120
1               0                0
0               1                0
1               0                0
0               0                1

'''

