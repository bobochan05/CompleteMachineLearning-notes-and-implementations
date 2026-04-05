'''
Bias-Variance Tradeoff in Polynomial Regression- Overfitting and Underfitting
how to choose the best degree in polynomial regression

Overfitting is when a model learns the noise in the training data instead of the underlying pattern.
Underfitting is when a model is too simple to capture the underlying pattern in the data.
To choose the best degree for polynomial regression
we can use techniques like cross-validation to evaluate model performance on unseen data.

we plot the graph of error vs model complexity(degree of polynomial) and
choose the degree where the error is minimized without overfitting for both training and test sets.



'''
#create the different order polynomial 
#split poly features into train and test sets
#fit on train set and evaluate on test set
#calculate the RSME for each degree for both train and test sets

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("C:\\Users\\soham\\Downloads\\Advertising.csv")
X=df[['TV','radio','newspaper']]
y=df['sales']

from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
rsme_test=[]
rsme_train=[]
for d in range(1,10):
 polynomial_converter=PolynomialFeatures(degree=d,include_bias=False)
 poly_features=polynomial_converter.fit_transform(X)
 X_train, X_test, y_train, y_test = train_test_split(poly_features, y, test_size=0.3, random_state=42)
 model=LinearRegression()
 model.fit(X_train,y_train)
 train_pred=model.predict(X_train)
 test_pred=model.predict(X_test)
 mse_train= mean_squared_error(y_train, train_pred)
 rsme_train.append(np.sqrt(mse_train))
 mse_test= mean_squared_error(y_test, test_pred)
 rsme_test.append(np.sqrt(mse_test))
 
print("RSME for train set:", rsme_train)
print("RSME for test set:", rsme_test)

plt.plot(range(1,6), rsme_train[0:5], label='Train RSME')
plt.plot(range(1,6), rsme_test[0:5], label='Test RSME')
plt.xlabel('Degree of Polynomial')
plt.ylabel('RSME')
plt.legend()

#finalising the model 
final_poly_converter=PolynomialFeatures(degree=3,include_bias=False)
final_poly_features=final_poly_converter.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(final_poly_features, y, test_size=0.3, random_state=42) 
final_model=LinearRegression()
final_model.fit(final_poly_features, y)

from joblib import dump, load  
dump(final_model, 'polynomialREG.joblib')
dump(final_poly_converter, 'polynomial_converter.joblib')

plt.show()

#loading the model
poly=load('polynomialREG.joblib')
new_data=np.random.randint(0,300,size=(5,3))
poly_converter=load('polynomial_converter.joblib')
new_data_poly=poly_converter.transform(new_data)
predictions=poly.predict(new_data_poly)
print("Predictions for new data:\n",predictions)






