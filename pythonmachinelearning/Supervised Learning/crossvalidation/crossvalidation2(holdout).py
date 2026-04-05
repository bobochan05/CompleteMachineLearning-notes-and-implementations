'''
here we divide the dataset into 3 parts 
1.train
2.validation
3.test
so there is no data leakage from test to train or validation set.
the test set is only used at the very end to evaluate the model's performance and not tune the hyperparameters

'''
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("C:\\Users\\soham\\Downloads\\Advertising.csv")
print(df.info()) # 200 rows and 4 columns
X=df[['TV','radio','newspaper']]
y=df['sales']
from sklearn.model_selection import train_test_split

#first splitting into train set and otherset 
X_train, X_other, y_train, y_other = train_test_split(X, y, test_size=0.3, random_state=101)
#so 70 percent of the data is in the train set and 30 percent in the other set
#now splitting the otherset into validation and test set
X_val, X_test, y_val, y_test = train_test_split(X_other, y_other, test_size=0.5, random_state=101)
#so 15 percent of the data is in the validation set and 15 percent in the test set

#now fitting the model to the train set 
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_val=scaler.transform(X_val)
X_test=scaler.transform(X_test)
#fitting only to train set and transforming all the sets 
from sklearn.linear_model import Ridge
model=Ridge(alpha=100)
model.fit(X_train,y_train)
#predicting on the validation set
y_val_pred=model.predict(X_val)
from sklearn.metrics import mean_squared_error
mse_val=mean_squared_error(y_val,y_val_pred)
print("Mean Squared Error on Validation Set:",mse_val)
#now based on predictions on validation set we update the alpha value 

#after finalizing the hyperparameters we evaluate on the test set
y_test_pred=model.predict(X_test)

