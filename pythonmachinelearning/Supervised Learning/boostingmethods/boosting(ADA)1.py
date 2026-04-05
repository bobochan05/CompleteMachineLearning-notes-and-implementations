import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\\Users\\soham\\Downloads\\mushrooms.csv")
print(df.info())
print(df['class'].value_counts())
print(df.head())
X=df.drop('class',axis=1)
X=pd.get_dummies(df , drop_first=True)
y=df['class']

from sklearn.model_selection import train_test_split  # If you see an import error, install scikit-learn: pip install scikit-learn
X_train,X_test ,y_train,y_test=train_test_split(X,y,test_size=0.15,random_state=101)

from sklearn.ensemble import AdaBoostClassifier
model=AdaBoostClassifier(n_estimators=1)
model.fit(X_train,y_train)

from sklearn.metrics import classification_report,ConfusionMatrixDisplay , confusion_matrix
y_preds=model.predict(X_test)
print(confusion_matrix(y_test,y_preds))
print(classification_report(y_test,y_preds))
print(ConfusionMatrixDisplay)
