'''this shows how to pivot a table
The pivot method reshapes data based on column values and reassignment of the index. Keep in mind, 
it doesn't always make sense to pivot data. In our machine learning lessons, 
we will see that our data doesn't need to be pivoted.
Pivot methods are mainly for data analysis,visualization, and exploration.'''
import numpy as np
import pandas as pd
df=pd.read_csv(r"C:\Users\soham\Downloads\Sales_Funnel_CRM.csv")
print(df)
#print(df.groupby(['Account Manager','Company','Contact']).mean(numeric_only=True))  Compute mean of numeric columns grouped by 'Account Manager')
# we can call the groupby function to help get more clarity on the topic
li=df[['Company','Product','Licenses']]
print(li)
print(pd.pivot(data=li,index='Company',columns='Product',values='Licenses'))
