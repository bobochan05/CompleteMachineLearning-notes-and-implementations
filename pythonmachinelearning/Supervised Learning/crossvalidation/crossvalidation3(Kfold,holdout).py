'''
here we split the dataset into 2 sets-
1.training set 
2.test set 

from the training set we further split into k-folds (here k=5)
we train the model on k-1 folds and validate on the remaining fold
this process is repeated k times, each time with a different fold as the validation set.
the average performance across all k iterations is used as the final performance metric.

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

from sklearn.model_selection import cross_val_score
#this returns the evaluation scores for each fold 
scores=cross_val_score(model,X_train,y_train,cv=5,scoring='neg_mean_squared_error')
print("Cross-Validation Scores (Negative MSE):",scores)
print("Average Cross-Validation Score (Negative MSE):",np.mean(scores))

#after we finalize the model we evaluate on the test set
model.fit(X_train,y_train)
y_test_pred=model.predict(X_test)
