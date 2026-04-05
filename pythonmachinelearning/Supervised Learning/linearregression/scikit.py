#scikit learn is a popular machine learning library in python
#it provides simple and efficient tools for data mining and data analysis
#it is built on numpy, scipy and matplotlib

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("C:\\Users\\soham\\Downloads\\Advertising.csv")
print(df.head())

#visualizing the relationship between each advertising medium and sales
fig,axes = plt.subplots(nrows=1,ncols=3,figsize=(16,6))

axes[0].plot(df['TV'],df['sales'],'o')
axes[0].set_ylabel("Sales")
axes[0].set_title("TV Spend")

axes[1].plot(df['radio'],df['sales'],'o')
axes[1].set_title("Radio Spend")
axes[1].set_ylabel("Sales")

axes[2].plot(df['newspaper'],df['sales'],'o')
axes[2].set_title("Newspaper Spend");
axes[2].set_ylabel("Sales")
plt.tight_layout()


#preparing the data for linear regression model
X=df[['TV','radio','newspaper']]
y=df['sales']

from sklearn.model_selection import train_test_split as tts
X_train, X_test, y_train, y_test = tts(X,y,test_size=0.3, random_state=42)
#the test size is 30% of the data , meaning 70% of the data is used for training the model and 30% for testing the model

from sklearn.linear_model import LinearRegression 
'''class LinearRegression(
    *,
    fit_intercept: bool = True,
    copy_X: bool = True,
    n_jobs: Int | None = None,
    positive: bool = False
)'''
model=LinearRegression()
model.fit(X_train,y_train)
print(model.predict(X_test))

plt.show()

