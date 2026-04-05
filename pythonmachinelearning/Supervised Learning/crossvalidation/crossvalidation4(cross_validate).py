'''
Cross Validation with cross_validate

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
from sklearn.linear_model import Ridge
model=Ridge(alpha=100)

from sklearn.model_selection import cross_validate
#this returns the evaluation scores for each fold along with fit time  and score time
scores = cross_validate(model,X_train,y_train,
                         scoring=['neg_mean_absolute_error','neg_mean_squared_error'],cv=5)
print(pd.DataFrame(scores))
'''
Fit_time : it is the time taken to fit the model on the training data for each fold.
eg- computing gradients , solving normal equations , building trees , updating weights etc.

Score_time : it is the time taken to evaluate the model on the validation data for each fold
eg- making predictions on the validation set and calculating the evaluation metrics

'''



