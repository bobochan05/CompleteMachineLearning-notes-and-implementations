'''
lasso regression implementation in Python. Lasso regression is a type of linear regression that uses L1 regularization to prevent overfitting.
It adds a penalty equal to the absolute value of the magnitude of coefficients multiplied by a regularization parameter to the loss function. 
This helps to shrink the coefficients of less important features towards zero,
effectively performing feature selection and improving model interpretability.
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

from sklearn.linear_model import LassoCV
lasso_model=LassoCV(eps=0.01, n_alphas=100, cv=5 , max_iter=1000)
#here eps is the length of the path , it is the ratio of the smallest alpha to the largest alpha
#n_alphas is the number of alphas along the regularization path
lasso_model.fit(X_train,y_train)
print(lasso_model.alpha_)#best alpha value found
test_pred=lasso_model.predict(X_test)
from sklearn.metrics import mean_squared_error
mse_test= mean_squared_error(y_test, test_pred)
rmse_test=np.sqrt(mse_test)
print("RSME for Lasso Regression on test set:", rmse_test)
print(lasso_model.coef_)

