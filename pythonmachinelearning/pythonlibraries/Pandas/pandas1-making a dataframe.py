'''a series is a data structure in Pandas that holds an array of information with 
a named index. 
the name index differentiates this from a simple numpy array '''
import numpy as np
import pandas as pd
#we use series by importing pd.series(), the first parameter is data and the second parameter is index 
mydata=[20,19,18,19]
myindex=['soham','goonja','archisman','masood']
#now initialising a series 
print(pd.Series(mydata,myindex))
#we can also type in data like this 
dict={'name':'soham','age':19,'year':2}#first making a dictionary
d=pd.Series(dict)
print(pd.Series(dict))
print(d['name'])
'''series mathods'''
dict1={'Japan':200,'swit':300,'france':250,'taiwan':400}
dict2={'Japan':250,'swit':500,'france':250,'china':400}
#we can performs arithmetic operaitons on panda series as they are derived form numpy arrays
s1=pd.Series(dict1)
s2=pd.Series(dict2)
print(s1*100)
print(s1+100)
print(s1/100)
print(s1+s2)
#we get NaN result for indexes which are not common
print(s1.add(s2,fill_value=0))
