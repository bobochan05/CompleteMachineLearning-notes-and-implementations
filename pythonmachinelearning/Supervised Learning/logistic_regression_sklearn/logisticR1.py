'''
ABOUT THE DATASET:

An experiment was conducted on 5000 participants to study the effects of age and physical health on hearing loss,
specifically the ability to hear high pitched tones. This data displays the result of the study in which participants were evaluated and scored for physical ability
and then had to take an audio test (pass/no pass) which evaluated their ability to hear high frequencies. The age of the user was also noted. 
Is it possible to build a model that would predict someone's liklihood to hear the high frequency sound based solely on their features (age and physical score)?

Features:
age= Age of participant in years
physical_score= Score achieved during physical exam

Label/Target:
test_result= 0 if no pass , = 1 if test passed
'''
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

df=pd.read_csv("C:\\Users\\soham\\Downloads\\hearing_test (1).csv")
#print(df.head())
#print(df.info())
#print(df.describe())
#print(df.value_counts('test_result'))

'''visualising the data by graphs
plt.figure()
sns.boxplot(x='test_result',y='physical_score',data=df,hue='test_result')
plt.figure()
sns.scatterplot(x='age',y='physical_score',data=df,hue='test_result')
plt.figure()
sns.pairplot(df,hue='test_result')
'''
#3D plot :
from mpl_toolkits.mplot3d import Axes3D 
fig = plt.figure()
ax = fig.add_subplot( projection='3d')
ax.scatter(df['age'],df['physical_score'],df['test_result'],c=df['test_result'])

#creating and training the model

#data preprocessing
X=df[['age','physical_score']]
y=df['test_result']
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.1,random_state=101)
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)

#model training
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(X_train,y_train)

#model predictions
predictions=model.predict(X_test)
print(predictions)


#plt.show()

