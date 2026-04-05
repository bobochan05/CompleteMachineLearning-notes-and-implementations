'''
pipelines chains together multiple steps so that the output of each step is used as input to the next step 
1.A Pipeline ensures that every preprocessing step is learned only from training data and applied consistently everywhere.
  we can code the preprocessing part everytime we build a model but that is risky and inconvinient.
  
'''
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

'''
suppose we want to first scale the features then make a simple model 

''' 
df=pd.read_csv("C:\\Users\\soham\\Downloads\\hearing_test (1).csv")
X=df[['age','physical_score']]
y=df['test_result']

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

#steps to give to the pipeline in order 
steps=[('scaling',StandardScaler()),('model',LogisticRegression())]
pipe=Pipeline(steps)

#train_test_split 
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y, test_size=0.33 , random_state=101)
pipe.fit(X_train, y_train)
pipe.predict(X_test)



