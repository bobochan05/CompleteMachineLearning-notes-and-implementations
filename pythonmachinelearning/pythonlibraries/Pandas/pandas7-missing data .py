'''dealing with missing data in pandas 
options for missing data:
1.keep
2.drop
3.fill'''
import pandas as pd
import numpy as np
#THE DATA:
#People were asked to score their opinions of actors from
# a 1-10 scale before and after watching one of their movies. However, some data is missing.
df=pd.read_csv(r"C:\Users\soham\Downloads\movie_scores (1).csv")
print(df)
#we can check for null values in a dataframe by using the funtion isnull()
print(df.isnull())
#if there are too many null values we can use notnull() for checking for filled values
print(df.notnull())
'''using the dropna() function we can remove any rows with null values
dropna(axis=0, how='any', thresh=None, subset=None, inplace=False) 
     axis : {0 or 'index', 1 or 'columns'}, default 0
        Determine if rows or columns which contain missing values are
        removed.
    
        * 0, or 'index' : Drop rows which contain missing values.
        * 1, or 'columns' : Drop columns which contain missing value.
        
    how : {'any', 'all'}, default 'any'
        Determine if row or column is removed from DataFrame, when we have
        at least one NA or all NA.
    
        * 'any' : If any NA values are present, drop that row or column.
        * 'all' : If all values are NA, drop that row or column.

    thresh : int, optional
        Require that many non-NA values. Cannot be used with how.

    subset : column label or sequence of labels, optional
        Only consider these columns for dropping. By default, use all columns.

    inplace : bool, default False
        If True, do operation inplace and return None.'''
        
print(df.dropna())#drops all rows with null values
print(df.dropna(axis=1))#drops all columns with null values
print(df.dropna(axis=0,how='all'))#drops all rows with all null values
print(df.dropna(thresh=5))#drops all rows with less than 5 non-null values
print(df.dropna(subset=['age','sex']))#drops all rows with null values in the age and sex columns

'''filling in the dataframe 
we use the fillna() function to fill in missing values
fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None)'''
#typically we will select a row then fill values in there 
print(df.fillna('missing data'))
#selecting a row then filling values in there
print(df.iloc[2].fillna('missing data'))
#we can also fill in values with the mean of the column
print(df.fillna(df.mean(numeric_only=True)))

