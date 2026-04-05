import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("C:\\Users\\soham\\Downloads\\mushrooms.csv")
X=df.drop('class',axis=1)
X=pd.get_dummies(df , drop_first=True)
y=df['class']

from sklearn.model_selection import train_test_split  # If you see an import error, install scikit-learn: pip install scikit-learn
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.15,random_state=101)

from sklearn.ensemble import GradientBoostingClassifier
model=GradientBoostingClassifier()
from sklearn.model_selection import GridSearchCV
n_estimators=[1,5,10]
learningrate=[0.1,0.05,0.2]
maxdepth=[3,4,5]
grid_model=GridSearchCV(estimator=model , param_grid = {
    "n_estimators": [50, 100],
    "max_depth": [3, 5]
}
)
grid_model.fit(X_train,y_train)

#predictions
y_preds=grid_model.predict(X_test)
from sklearn.metrics import classification_report,confusion_matrix
cm=confusion_matrix(y_test,y_preds)
cr=classification_report(y_test,y_preds)
print(cm)
print(cr)
