import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("C:\\Users\\soham\\Downloads\\cement_slump.csv")
print(df.head())
X = df.drop('Compressive Strength (28-day)(Mpa)',axis=1)
y = df['Compressive Strength (28-day)(Mpa)']

#train_test_split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_X_train = scaler.fit_transform(X_train)
scaled_X_test = scaler.transform(X_test)
'''
Support Vector Machines - Regression
There are three different implementations of Support Vector Regression: SVR, NuSVR and LinearSVR. 
LinearSVR provides a faster implementation than SVR but only considers the linear kernel,
while NuSVR implements a slightly different formulation than SVR and LinearSVR.

Difference between the different regression types 
1.linearSVR is more efficient than SVR when dealing with large datasets
2.SVR allows the use of different kernel functions (like RBF, polynomial, etc.)

'''
#now making the model 
from sklearn.svm import SVR ,LinearSVR
base_model = SVR()
base_model.fit(scaled_X_train, y_train)

from sklearn.metrics import mean_squared_error
y_pred = base_model.predict(scaled_X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error (MSE) of base SVR model:", mse)

#performing gridsearch to find the best hyperparameters for SVR
from sklearn.model_selection import GridSearchCV
param_grid = {
    'C': [0.1, 1, 10],
    'gamma': ['scale', 'auto'],
    'kernel': ['rbf', 'linear']
}
'''
here,
C is the parameter that controls the trade-off between achieving a low training error and a low testing error.
gamma defines how far the influence of a single training example reaches, with low values meaning 'far' and high values meaning 'close'.
kernel specifies the type of kernel to be used in the algorithm.
'''
grid_model = GridSearchCV(estimator=base_model, param_grid=param_grid, cv=5)
grid_model.fit(scaled_X_train, y_train)
print("Best Hyperparameters:", grid_model.best_params_)

#evaluating the grid model
y_pred_grid = grid_model.predict(scaled_X_test)
mse_grid = mean_squared_error(y_test, y_pred_grid)
print("Mean Squared Error (MSE) of grid search SVR model:", mse_grid)

'''
you cannot use Elastic Net in the standard SVR or NuSVR classes in Scikit-Learn.

Standard SVR (which uses kernels like RBF) is mathematically built around L2 Regularization.

It does not support L1 (Lasso) or Elastic Net penalties because L1 regularization makes the "kernel trick" 
(the math that allows non-linear curved lines) extremely difficult or impossible to calculate efficiently.

However, if you are okay with a Linear model (straight lines only), you can do this using SDGRregressor

'''



