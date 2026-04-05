'''residual plots help in identifying non-linearity, unequal error variances, and outliers in regression analysis.
they help us understand if linear regression is appropriate for our data or not
A residual plot displays the residuals on the vertical axis and the independent variable on the horizontal axis.
If the residuals are randomly dispersed around the horizontal axis,it indicates that a linear regression model is appropriate for the data.
If there is a discernible pattern (like a curve) in the residual plot
it suggests that a non-linear model may be more suitable.'''

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  

df=pd.read_csv("C:\\Users\\soham\\Downloads\\Advertising.csv")
# print(df.info())

#transforming the data
X=df[['TV','radio','newspaper']]
y=df['sales']
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=42)

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X_train,y_train)

#error metrics calculation 
from sklearn.metrics import mean_absolute_error, mean_squared_error

test_predictions=model.predict(X_test)
#comparing the predicted values with the actual values
mae=mean_absolute_error(y_test,test_predictions)
mse=mean_squared_error(y_test,test_predictions)
rmse=np.sqrt(mse)
print("Mean Absolute Error:",mae)
print("Mean Squared Error:",mse)
print("Root Mean Squared Error:",rmse)

'''how to check if the error is good or bad?
one way to do this is to compare the rmse with the mean of the target variable
if the rmse is significantly lower than the mean of the target variable then the model is performing well
otherwise the model may need improvement.'''

#residual plot
residuals=y_test - test_predictions
sns.scatterplot(x=test_predictions, y=residuals)
plt.axhline(0, color='red', linestyle='--')
sns.displot(residuals,bins=20, kde=True)
plt.show()

#by seeing the residualplot we can see that linear regression model is appropriate for the given data 

 