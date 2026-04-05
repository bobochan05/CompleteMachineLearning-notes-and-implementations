
linktotheofficialdocument = "https://arxiv.org/pdf/1603.02754.pdf"


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix

from xgboost import XGBClassifier

df = pd.read_csv(
    "C:\\Users\\soham\\Downloads\\bank+marketing\\bank-full.csv",
    sep=";"
)

print(df.head())
print(df.info())
print(df['y'].value_counts())

# Convert target to binary FIRST (important)
y = df["y"].map({"yes": 1, "no": 0})
X = df.drop("y", axis=1)
X = pd.get_dummies(X, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=101,
    stratify=y   # keeps class balance
)
print(df['y'].value_counts())

from xgboost import XGBClassifier
model=XGBClassifier(n_estimators=100 ,max_depth=4 )
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
# Force clean integer labels (prevents sklearn error)
y_pred = y_pred.astype(int)

from sklearn.metrics import classification_report,confusion_matrix
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))



