'''working with rows in a data frame
1.how to assign a new INDEX or how to make a column the index'''
import numpy as np
import pandas as pd

file=pd.read_csv(r"C:\Users\soham\Downloads\tips.csv")
file=file.set_index('Payment ID')#the set_index permanently sets the Payment ID as the index

#grabbing a row 
#we can grab a row by different functions like iloc() 
# print(file.iloc[0]) ,this is not used normally as one wouldnt know the required index number
#to print a row we mostly use loc to find a particular row by passing the row name as argument
print(file.loc['Sun2959'])

#we can grab multiple rows by slicing 
print(file.iloc[0:5])

#removing a row 
#we remove a row by using the same drop method 
print(file.drop('Sun2959'))#this is not permanent to make it permanent we use: file=file.drop('Sun2959')

#to add a new row we need to make sure it fits the right dimensions


