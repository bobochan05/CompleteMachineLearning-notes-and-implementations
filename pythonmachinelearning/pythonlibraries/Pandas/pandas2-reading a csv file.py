'''data-frames , they are essentially multiple row of information
with a single index'''
import numpy as np
import pandas as pd
#making an 2d-array
np.random.seed(100)
data=np.random.randint(0,50,(3,3))
print(data)
#now transforming this into a data structure 
name=['SD','GD','MSS']
month=['JAN','FEB','MARCH']
data_frame=pd.DataFrame(data,name,month)
print(data_frame)
#this is the method to create a data structure
#but realistically we would be reading the data from a file 
'''reading a data from a file 
1.reading a .csv file -a file where information is separated by a comma'''
#for reading a csv file first we need to find where our python code is located
#2nd where the csv file is located
file=pd.read_csv(r"C:\Users\soham\Downloads\tips.csv")
print(file)
print(file.columns)#we use the coloums method to just check the different column names
#we can use the head function to see the first few rows
print(file.head())#we can also pass an argument in the head to see that number of columns
#we can use the tail function to see the last few rows

#we can use the describe function to see essential data like the mean , median , highest , lowest etc 
print(file.describe().transpose())#the transpose function makes a transpose matrix of for a better view



