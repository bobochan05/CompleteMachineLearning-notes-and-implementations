import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df=pd.read_csv("C:\\Users\\soham\\Downloads\\data_banknote_authentication.csv")
print(df.info())
X=df.drop('Class',axis=1)
y=df['Class']

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.3, random_state=101)

from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier()
model.fit(X_train,Y_train)

from sklearn.model_selection import GridSearchCV
n_estimators=[10,30,60,100,128,200]
max_features= [2,3,4]
bootstrap = [True,False]
param_grid = {'n_estimators':n_estimators,
             'max_features':max_features,
             'bootstrap':bootstrap,
             } 

grid_model=GridSearchCV(estimator=model , param_grid=param_grid)
grid_model.fit(X_train,Y_train)
print(grid_model.best_estimator_)
grid_model.best_params_



from sklearn.metrics import confusion_matrix,classification_report
Y_preds=grid_model.predict(X_test)
cm=confusion_matrix(Y_preds,Y_test)
cr=classification_report(Y_preds,Y_test)
print("confusion matrix :\n",cm)
print("classification report :\n",cr)


