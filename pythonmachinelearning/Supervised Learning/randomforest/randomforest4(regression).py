import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("C:\\Users\\soham\\Downloads\\rock_density_xray.csv")
print(df.info())
df.columns=['Signal','Density'] #renaming the features
sns.scatterplot(x='Signal', y='Density' , data=df) 
X=df.drop('Density',axis=1)
y=df['Signal']
from sklearn.model_selection import train_test_split
X_train , X_test , Y_train, Y_test=train_test_split(X, y , test_size=0.3 , random_state=101)

# trying linear regression on the data 
from sklearn.linear_model import LinearRegression
model_LR=LinearRegression()
model_LR.fit(X_train,Y_train)
y_preds1=model_LR.predict(X_test)

#trying SVR on the data 
from sklearn.svm import SVR
model_SVR=SVR()
model_SVR.fit(X_train,Y_train)
y_preds3=model_SVR.predict(X_test)

#trying polynomial regression on the data 
from sklearn.preprocessing import PolynomialFeatures
poly_converter=PolynomialFeatures(degree=5 , include_bias=False)
X=poly_converter.fit_transform(X)
from sklearn.model_selection import train_test_split
X_train , X_test , Y_train, Y_test=train_test_split(X, y , test_size=0.3 , random_state=101)
from sklearn.linear_model import LinearRegression
model_PR=LinearRegression()
model_PR.fit(X_train , Y_train)
y_preds2=model_PR.predict(X_test)

from sklearn.metrics import mean_squared_error
print(np.sqrt(mean_squared_error(Y_test,y_preds1)))
print(np.sqrt(mean_squared_error(Y_test,y_preds2)))
print(np.sqrt(mean_squared_error(Y_test,y_preds3)))


