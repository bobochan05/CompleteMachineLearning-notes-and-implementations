import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures

# Load data
df = pd.read_csv(r"C:\Users\soham\Downloads\rock_density_xray.csv")
df.columns = ['Signal', 'Density']

# Correct X and y
X = df[['Signal']]
y = df['Density']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=101
)

def run_model(model, X_train, y_train, X_test, y_test):
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    print(f"RMSE: {rmse}")

    signal_range = np.arange(0, 100).reshape(-1, 1)
    output = model.predict(signal_range)

    plt.figure(figsize=(12,6), dpi=150)
    sns.scatterplot(x='Signal', y='Density', data=df, color='black')
    plt.plot(signal_range, output, color='red')
    plt.show()

    
sns.scatterplot(x='Signal', y='Density' , data=df) 
X = df[['Signal']]
y = df['Density']
from sklearn.model_selection import train_test_split
X_train , X_test , Y_train, Y_test=train_test_split(X, y , test_size=0.3 , random_state=101)

# trying linear regression on the data 
from sklearn.linear_model import LinearRegression
model_LR=LinearRegression()
model_LR.fit(X_train,Y_train)
y_preds1=model_LR.predict(X_test)
'''GRAPH1'''
run_model(model_LR,X_train,Y_train,X_test,Y_test)

#trying SVR on the data 
from sklearn.svm import SVR
model_SVR=SVR()
model_SVR.fit(X_train,Y_train)
y_preds3=model_SVR.predict(X_test)
'''GRAPH2'''
run_model(model_SVR,X_train,Y_train,X_test,Y_test)


from sklearn.metrics import mean_squared_error
print(np.sqrt(mean_squared_error(Y_test,y_preds1)))

print(np.sqrt(mean_squared_error(Y_test,y_preds3)))


from sklearn.ensemble import RandomForestRegressor
model_RFR=RandomForestRegressor(n_estimators=100)
model_RFR.fit(X_train,Y_train)
y_preds2=model_RFR.predict(X_test)
run_model(model_RFR,X_train,Y_train,X_test,Y_test)


