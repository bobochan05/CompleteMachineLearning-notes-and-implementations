import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns   
df=pd.read_csv("C:\\Users\\soham\\Downloads\\Advertising.csv")
print(df.head())
X=df[['TV','radio','newspaper']]
y=df['sales']

