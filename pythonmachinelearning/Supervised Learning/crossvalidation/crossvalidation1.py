'''
previously crossvalidation was done for us automatically by sklearn's model_selection module.
here we implement it manually to understand how it works.
we will use k-fold crossvalidation to evaluate a model's performance.

'''
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

df=pd.read_csv("C:\\Users\\soham\\Downloads\\Advertising.csv")

from sklearn.model_selection import train_test_split
X=df[['TV','radio','newspaper']]
y=df['sales']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=101)

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)

from sklearn.linear_model import Ridge
model=Ridge(alpha=100)
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
from sklearn.metrics import mean_squared_error
mse=mean_squared_error(y_test,y_pred)
print(mse)

'''limitations of train_test_split:
1. variability in results: different random splits can lead to different performance estimates.
2. inefficient use of data: only a portion of the data is used for training in each
3. leakage of information: if the test set is used to tune hyperparameters, it can lead to overfitting.'''