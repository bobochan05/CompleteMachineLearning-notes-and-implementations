# Official XGBoost paper
linktotheofficialdocument = "https://arxiv.org/pdf/1603.02754.pdf"

# ===============================
# Imports
# ===============================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix

from xgboost import XGBClassifier

# ===============================
# Load Dataset
# ===============================
df = pd.read_csv(
    "C:\\Users\\soham\\Downloads\\bank+marketing\\bank-full.csv",
    sep=";"
)

print(df.head())
print(df.info())

# ===============================
# Target & Features
# ===============================
# Convert target to binary FIRST (important)
y = df["y"].map({"yes": 1, "no": 0})

# Drop target from features
X = df.drop("y", axis=1)

# One-hot encode categorical variables
X = pd.get_dummies(X, drop_first=True)

# ===============================
# Train-Test Split
# ===============================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=101,
    stratify=y   # keeps class balance
)

# ===============================
# Base XGBoost Model
# ===============================
xgb_model = XGBClassifier(
    
)

# ===============================
# Hyperparameter Grid
# ===============================
param_grid = {
    "n_estimators": [50, 100, 150],
    "learning_rate": [0.05, 0.1, 0.2],
    "max_depth": [3, 4, 5]
}

# ===============================
# Grid Search
# ===============================
grid_model=GridSearchCV(
    estimator=xgb_model,
    param_grid=param_grid,
    scoring="recall",
    cv=5,
    n_jobs=-1
)


grid_model.fit(X_train, y_train)

# ===============================
# Best Model
# ===============================
print("Best Parameters:", grid_model.best_params_)

best_model = grid_model.best_estimator_

# ===============================
# Predictions (IMPORTANT FIX)
# ===============================
y_pred = best_model.predict(X_test)

# Force clean integer labels (prevents sklearn error)
y_pred = y_pred.astype(int)

# ===============================
# Evaluation
# ===============================
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
