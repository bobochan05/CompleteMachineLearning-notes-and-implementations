'''groupby() operations in python is used to split the data into groups based 
on some criteria, apply a function to each group, and combine the results back into a DataFrame.
This is useful for data analysis and aggregation tasks.'''
import numpy as np
import pandas as pd
df=pd.read_csv(r"C:\Users\soham\Downloads\mpg.csv")
print(df)
'''mean(): Compute mean of groups
sum(): Compute sum of group values
size(): Compute group sizes
count(): Compute count of group
std(): Standard deviation of groups
var(): Compute variance of groups
sem(): Standard error of the mean of groups
describe(): Generates descriptive statistics
first(): Compute first of group values
last(): Compute last of group values
nth() : Take nth value, or a subset if n is a list
min(): Compute min of group values
max(): Compute max of group values '''
print(df.groupby('model_year').mean(numeric_only=True))  # Compute mean of numeric columns grouped by 'model_year')
#we can groupby multiple columns
print(df.groupby(['model_year', 'cylinders']).mean(numeric_only=True))


'''multiindexing with a new dataframe '''

df2=df.groupby(['model_year', 'cylinders']).mean(numeric_only=True)
print(df2.index.names)
print(df2.head())
#grabbing based on outisde index 
print(df2.loc[70])  
print(df2.loc[[70,72]])
#grabbing a particular column 
print(df2.loc[(70 ,4)])

'''Grab Based on Cross-section with .xs()
This method takes a key argument to select data at a particular level of a MultiIndex.

Parameters
key : label or tuple of label
    Label contained in the index, or partially in a MultiIndex.
axis : {0 or 'index', 1 or 'columns'}, default 0
    Axis to retrieve cross-section on.
level : object, defaults to first n levels (n=1 or len(key))
    In case of a key partially contained in a MultiIndex, indicate
    which levels are used. Levels can be referred by label or position.'''

print(df2.xs(key=70, level='model_year'))  # Grabs all data for model_year 70

#if we want to grab '4 cylinders' from all columns we cant easily do that using loc() so we use xs()
print(df2.xs(key=4,level='cylinders'))  
#if we want to grab 6,8 from all columns it is better to drop the 4 cylinder from all columns 
print(df2.drop(index=4, level='cylinders'))  # Drops all rows with 4 cylinders

#we can use sort_index() to sort them in ascending or desending order 
print(df2.sort_index(level='model_year', ascending=False))

'''agg() is very powerful,allowing you to pass in a dictionary
where the keys are the columns and the values are a list of aggregate methods.'''

print(df2.agg({'mpg':['mean', 'min', 'max'] , 'weight':['sum', 'min', 'max'], 'acceleration':['max','mean','min']}))
#agg with groupby
print(df.groupby('model_year').agg({'mpg':['median','mean'],'weight':['mean','std']}))