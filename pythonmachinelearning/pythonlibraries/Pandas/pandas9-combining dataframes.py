'''combining data frames - concatenation 
its important that the columns are matching '''
import numpy as np
import pandas as pd 
d1={'A':['a','b','c'] , 'B':[1,2,3]}
d2={'C':['d','e','f'] , 'D':[4,5,6]}
df1=pd.DataFrame(d1)
df2=pd.DataFrame(d2)
print(df1)
print(df2)
print(pd.concat([df1, df2], axis=1))

'''merging data frames - similar to SQL joins '''

registrations = pd.DataFrame({'reg_id':[1,2,3,4],'name':['Andrew','Bobo','Claire','David']})
logins = pd.DataFrame({'log_id':[1,2,3,4],'name':['Xavier','Andrew','Yolanda','Bobo']})

'''pd.merge()
The join is done on columns or indexes. If joining columns on
columns, the DataFrame indexes *will be ignored*. Otherwise if joining indexes
on indexes or indexes on a column or columns, the index will be passed on.'''

#inner merge 
#by inner merge we only take things present in both groups that means it is like an intersection
print(pd.merge(registrations,logins ,how='inner',on='name'))

#left and right merge 
#order of the dataframe passed matters here 
print(pd.merge(registrations,logins,how='left',on='name')) 
#here we keep all the information of registations , it is like a ven diagram between registrations and logins 
#where we take the intersection + all elements of registration 

#if we switch order then :
print(pd.merge(logins,registrations,how='left',on='name'))
#here we keep all the information of logins , it is like a ven diagram between registrations and logins
#where we take the interesction + all elements of logins

#outer merge 
#by outer merge we include everything from both dataframes essentially a ven diagram where whole thing is selected 
df=pd.merge(registrations,logins,how='outer',on='name')
df=df.set_index('name')
print(df)


