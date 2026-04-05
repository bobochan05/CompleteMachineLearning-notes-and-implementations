'''
we need to scale out data to improve the performance of our model.
Scaling techniques like Standardization and Normalization help in bringing all features to a similar scale
which is particularly important for algorithms that rely on distance calculations or gradient descent optimization.

'''
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("C:\\Users\\soham\\Downloads\\Advertising.csv")
X=df[['TV','radio','newspaper']]
y=df['sales']

#first we will make new polynomial features

from sklearn.preprocessing import PolynomialFeatures
polynomial_converter=PolynomialFeatures(degree=3,include_bias=False)
poly_features=polynomial_converter.fit_transform(X)

#now we will split the data into training and testing sets

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(poly_features, y, test_size=0.3, random_state=42)

#now we will scale the data

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
scaler.fit(X_train)
X_train=scaler.transform(X_train)
X_test=scaler.transform(X_test)




