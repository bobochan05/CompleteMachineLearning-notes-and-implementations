'''
KNN nearest neighbour classifier is the simplest machine learning algorithm.
It requires no training phase and is used for both classification and regression.
It works by finding the K nearest data points in the training set to a given test point
and making predictions based on the majority class (for classification) or average value (for regression) of those neighbors.

'''
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("C:\\Users\\soham\\Downloads\\gene_expression.csv")
print(df.head())
X = df.drop('Cancer Present',axis=1)
y = df['Cancer Present']
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=101)

from sklearn.preprocessing import StandardScaler
Scaler=StandardScaler()
X_train=Scaler.fit_transform(X_train)
X_test=Scaler.transform(X_test)

from sklearn.neighbors import KNeighborsClassifier
Knn=KNeighborsClassifier(n_neighbors=1)
Knn.fit(X_train,y_train)

y_pred=Knn.predict(X_test)

'''
a pipeline is a sequence of data processing components.
A pipeline is a sequence of transformers + a final estimator, where:
Transformers: modify data (fit + transform)
Estimator: learns & predicts (fit + predict)
In Python, this is most commonly done using scikit-learn
'''
from sklearn.pipeline import Pipeline
operations=[('scaler',Scaler),('knn',Knn)] #this means first scaler will be applied then knn will be applied 
pipe=Pipeline(operations)

from sklearn.model_selection import GridSearchCV
k_values=list(range(1,20))

'''
Note: If your parameter grid is going inside a PipeLine, your parameter name needs to be specified in the following manner:*

chosen_string_name + two underscores + parameter key name
model_name + __ + parameter name
knn_model + __ + n_neighbors
knn_model__n_neighbors

'''
param_grid={'knn__n_neighbors':k_values}
full_cv_classifier = GridSearchCV(pipe,param_grid,cv=5,scoring='accuracy')
full_cv_classifier.fit(X_train,y_train)
print("Best K value: ",full_cv_classifier.best_params_)
final_model=full_cv_classifier.best_estimator_
final_pred=final_model.predict(X_test)






