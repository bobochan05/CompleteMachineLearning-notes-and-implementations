import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df=pd.read_csv("C:\\Users\\soham\\Downloads\\penguins_size (1).csv")
#print(df.head())
#print(df.info())
#print(df.dropna().isnull().sum())
df=df.dropna()
print(df.head())
print(df.groupby('species').mean(numeric_only=True))

#creating dummy variables 
X=pd.get_dummies(df.drop('species',axis=1) , drop_first=True)
y=df['species']

#training the model 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier()
model.fit(X_train,y_train)

#evaluating the model 
from sklearn.metrics import confusion_matrix,classification_report
base_pred = model.predict(X_test)
cm=confusion_matrix(base_pred,y_test)
cr=classification_report(base_pred,y_test)

#we can use feature importance to check the importance of each feature 
#they are given in the exact order of the our dataset 
print(model.feature_importances_)

#plotting the decision tree
from sklearn.tree import plot_tree

def report_model(model):
    model_preds = model.predict(X_test)
    print(classification_report(y_test,model_preds))
    print('\n')
    plt.figure(figsize=(12,8),dpi=150)
    plot_tree(model,filled=True,feature_names=X.columns)
    plt.show()

report_model(model)






