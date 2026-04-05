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

'''Evaluating the model performance using different metrics
TYPES OF ERRORS
1. Mean Absolute Error(MAE)
   this is the average of absolute differences between predicted and actual values.this often does not take
   the outliers into account and gives equal weight to all errors.
2. Mean Squared Error(MSE)
    this is the average of squared differences between predicted and actual values.this gives more weight to larger errors
    making it more sensitive to outliers.but it is not in the same unit as the target variable.
3. Root Mean Squared Error(RMSE)
    this is the square root of the mean squared error.it is in the same unit as the target variable and is more interpretable.
'''
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


