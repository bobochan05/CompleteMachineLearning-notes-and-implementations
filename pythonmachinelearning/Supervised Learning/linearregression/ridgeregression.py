'''
ridge regression is a type of linear regression that includes a regularization term to prevent overfitting.
It adds a penalty equal to the square of the magnitude of coefficients multiplied by a regularization parameter
to the loss function. This helps to shrink the coefficients of less important features towards zero,
thereby reducing model complexity and improving generalization on unseen data.

'''

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

df=pd.read_csv("C:\\Users\\soham\\Downloads\\Advertising.csv")
X=df[['TV','radio','newspaper']]
y=df['sales']

from sklearn.preprocessing import PolynomialFeatures
polynomial_converter=PolynomialFeatures(degree=3,include_bias=False)
poly_features=polynomial_converter.fit_transform(X)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(poly_features, y, test_size=0.3, random_state=42)

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
scaler.fit(X_train)
X_train=scaler.transform(X_train)
X_test=scaler.transform(X_test)

from sklearn.linear_model import Ridge
ridge_model=Ridge(alpha=10)
ridge_model.fit(X_train,y_train)

test_pred=ridge_model.predict(X_test)

from sklearn.metrics import mean_squared_error
mse_test= mean_squared_error(y_test, test_pred)
rmse_test=np.sqrt(mse_test)
print("RSME for Ridge Regression on test set:", rmse_test)

#ridge regression with different alpha values

from sklearn.linear_model import RidgeCV
ridgeCV_model=RidgeCV(alphas=[0.1,1.0,3,4 ,5,6,10.0,100.0])
ridgeCV_model.fit(X_train,y_train)
print("Best alpha value found:", ridgeCV_model.alpha_)
test_pred_cv=ridgeCV_model.predict(X_test)
mse_test_cv= mean_squared_error(y_test, test_pred_cv)
rmse_test_cv=np.sqrt(mse_test_cv)
print("RSME for RidgeCV Regression on test set:", rmse_test_cv)


