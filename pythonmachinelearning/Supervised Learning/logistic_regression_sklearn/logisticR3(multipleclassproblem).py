'''
multiclass classification using Logistic Regression
1.input the dataframe
2.split the dataset into training and testing sets
3.scale the training sets 
4.make an instance model of logistic regression 
5.make an instance model of logistic regression with gridsearch to find the best parameters

'''
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

df=pd.read_csv("C:\\Users\\soham\\Downloads\\Iris.csv")
print(df.head())
print(df.info())
X=df.drop('species',axis=1)
y=df['species']

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=101)
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)

#model training
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
model=LogisticRegression(solver='saga',max_iter=5000)
'''
parameters:
1.solver='sage' : The solver is the optimization algorithm used to find the best coefficients.
What SAGA does?
It is a stochastic gradient based solver. It Works well for large datasets , Supports regularization:

2."ovr" : This parameter specifies the strategy for handling multiclass classification.
One-vs-Rest (OvR) is a common approach where a binary classifier is trained for each class against all other classes.
(OvR) is mostly used when the dataset is sparse

3.max_iter=5000 : This sets the maximum number of iterations for the solver to converge.
Higher values allow more time for convergence but may increase computation time.


OTHER STRATEGIES:
- 'multinomial': This strategy treats the problem as a single optimization problem, considering all classes simultaneously. 
It is often more accurate than OvR for multiclass problems but may require more computational resources.

OVSR vs MULTINOMIAL: when to use which?
- Use OvR when you have a large number of classes or when the dataset is sparse.
- Use Multinomial when you have a smaller number of classes and want potentially better accuracy.

Why OvR is mostly used when there are a lot of classes?
- Computational Efficiency: Training a separate binary classifier for each class can be more efficient 
                            than training a single multinomial classifier, especially when the number of classes is large.

In sklearn 1.8 and later, the default value for multi_class is 'auto', which automatically selects the appropriate strategy based on the data.
so we dont have to pass multi_class parameter explicitly.
'''
# Penalty Type
penalty = ['elasticnet']
# Use logarithmically spaced C values (recommended in official docs)
# here C values are the inverse of regularization strength. They control the trade-off between fitting the training data well 
# and keeping the model coefficients small to avoid overfitting.
C = np.logspace(0, 4, 10)
grid_params = {'penalty': penalty, 'C': C}
grid_model=GridSearchCV(estimator=model,
                         param_grid=grid_params,
                        scoring='accuracy',
                        cv=5,
                        verbose=2)


grid_model.fit(X_train,y_train)


#evaluating the model
from sklearn.metrics import classification_report,confusion_matrix
y_pred1=grid_model.predict(X_test)
print("CLASSIFICATION REPORT")
print(classification_report(y_test,y_pred1))

