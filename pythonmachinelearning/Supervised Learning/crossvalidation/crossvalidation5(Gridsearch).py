'''
grid-search for hyperparameter tuning
Grid Search is a method to systematically find the best hyperparameters
for a machine-learning model using cross-validation.

'''
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("C:\\Users\\soham\\Downloads\\Advertising.csv")
X=df[['TV','radio','newspaper']]
y=df['sales']
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=101)
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)

from sklearn.linear_model import ElasticNet
base_model=ElasticNet()
from sklearn.model_selection import GridSearchCV
#defining the hyperparameter grid to search
param_grid={'alpha':[0.1,1.0,10.0,100.0],'l1_ratio':[.1,.5,.7,.9,.95,.99,1]}
Grid_model=GridSearchCV(estimator=base_model,
                        param_grid=param_grid,
                        scoring='neg_mean_squared_error',
                        cv=5,  verbose=2   )#verbose is the no of information printed out 

Grid_model.fit(X_train,y_train)
# print("Best Hyperparameters:",Grid_model.get_params())
print(Grid_model.best_estimator_)
print(Grid_model.best_params_)

y_pred=Grid_model.predict(X_test)

