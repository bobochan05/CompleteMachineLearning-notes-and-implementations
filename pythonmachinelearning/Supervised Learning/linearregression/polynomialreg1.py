''' 
polynomial regression is used to model the relationalship when a linear model is not sufficient 
to capture the underlying trend of the data.

Interaction Parameter: What if features are only significant when in sync with one another 
(eg: x1 and x2 together have an effect, but individually they do not)?
(eg:newspaper spend is not effective in itself but it is effective when added to tv advertisement)
In such cases, we can create interaction terms by multiplying the features together.
Scikit-learn's PolynomialFeatures can be used to generate these interaction terms automatically.
from sklearn.preprocessing import PolynomialFeatures

'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df=pd.read_csv("C:\\Users\\soham\\Downloads\\Advertising.csv")
X=df[['TV','radio','newspaper']]
y=df['sales']

from sklearn.preprocessing import PolynomialFeatures
polynomial_converter=PolynomialFeatures(degree=2,include_bias=False)
poly_features=polynomial_converter.fit_transform(X)
print(poly_features)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(poly_features, y, test_size=0.3, random_state=42)

from sklearn.linear_model import LinearRegression
model =LinearRegression()
model.fit(X_train,y_train)

from sklearn.metrics import mean_absolute_error, mean_squared_error 
mse= mean_squared_error(y_test, model.predict(X_test))
mae= mean_absolute_error(y_test, model.predict(X_test))
rsme= np.sqrt(mse)
print("MAE:", mae)
print("MSE:", mse)
print("RSME:", rsme)

