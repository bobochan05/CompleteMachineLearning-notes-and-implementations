'''
choosing a kernel depends on the dataset -
if your data is linearly separable we mostly use a linear kernel to not overcomplicate thing 

Kernel=rbf(radial basis function)

When training an SVM with the Radial Basis Function (RBF) kernel, two parameters must be considered: C and gamma.
The parameter C, common to all SVM kernels, trades off misclassification of training examples against simplicity of the decision surface. 
A low C makes the decision surface smooth, while a high C aims at classifying all training examples correctly.
gamma defines how much influence a single training example has. The larger gamma is, the closer other examples must be to be affected.

'''
import svm1
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df=pd.read_csv("C:\\Users\\soham\\Downloads\\mouse_viral_study.csv")
print(df.info())
X=df.drop('Virus Present',axis=1)
y=df['Virus Present']

from sklearn.svm import SVC
model=SVC(kernel='rbf' , C=1,gamma=0.1)
model.fit(X,y)
'''
we have to do grid search to find the best hyperparameters i.e C , gamma
'''
#applying grid search to the mdoel
from sklearn.model_selection import GridSearchCV
gamma=np.linspace(0.01 , 1.5 ,20)
param_grid = {'C':[0.01,0.1,1],'gamma':gamma,'kernel':['linear','rbf']}
grid_model=GridSearchCV(estimator=model, param_grid=param_grid ,)
grid_model.fit(X,y)
grid_model.best_estimator_



svm1.plot_svm_boundary(grid_model.best_estimator_,X,y)
