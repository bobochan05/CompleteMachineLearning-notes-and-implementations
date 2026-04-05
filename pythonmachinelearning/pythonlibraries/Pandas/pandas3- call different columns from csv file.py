'''methods , how to call different columns of a series'''
#we use the same method we used in numpy to call a column
import numpy as np
import pandas as pd

file=pd.read_csv(r"C:\Users\soham\Downloads\tips.csv")
print(file['total_bill'])#we only call the total bill column 
#to see multiple columns we store the column names in a list and pass the list as an argument 
columns_=['total_bill','tip','sex']
print(file[columns_])#or we can directly pass the list as an argument with double brackets
'''we can also perform arithmetic operations between 2 columns
we can also add a new column to the file by passing an argument and assigning it the value '''
file['bill+tip']=file['total_bill']+file['tip']#a new coloums "bill+tip" is created
print(file)#if you reference a column that already exits it will update the column and not make a new one 
#we can use the np.round() function to round off values
file['bill+tip']=np.round(file['bill+tip'],1)
print(file)
#we can also remove any column we need by the drop() function
print(file.drop(['total_bill','tip'],axis=1))#removed total_bill and tip from column, the default axis is axis=0 which is row 
#this drop() method is not permanent if we call file after this it will still show 12 columns
#to make the removal permanent we pass an argument 'inplace=True'
# file.drop('tip',inplace=True)#permanently deletes tip


 