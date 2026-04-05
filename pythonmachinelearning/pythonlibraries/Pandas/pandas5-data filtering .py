'''this is about data filtering in real case our data will be too big to filter based on position
we filter on condition
1.organising our data, the format for ML is axis=0 or rows , should have the instances 
and axis=1 or columns , should have the features or attributes
for example if we want to work on a particular attribute we grab the specific column and filter'''
import numpy as np
import pandas as pd

file=pd.read_csv(r"C:\Users\soham\Downloads\tips.csv")
file=file.set_index('Payment ID')
print(file)
#for example if we want to filter the total bill column for only values over 40 dollars 
#first we select the column
#true=file['total_bill'] > 40 , true will hold all the indexes where boolean value if True 
#print(file[true])

#we can also do this by directly using:
print(file[file['total_bill']>40])#temporary

'''filtering by many conditions by using AND and OR operator '''
print(file[(file['total_bill']> 40) & (file['sex']=='Male')])#both condition ture
print(file[(file['total_bill']> 40) | (file['sex']=='Male')])#one condition true

#if a value happens to be in a list of option it is tedious to pass the column argument everytime
#if we need to check for sat , sun , mon 
#we make a list of options 
days=['Sat','Sun','Mon']
#we use the isin() method to check 
print(file['day'].isin(days))