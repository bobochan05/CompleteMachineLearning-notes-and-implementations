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
'''
SVC (Support Vector Classification) is a type of Support Vector Machine (SVM) algorithm used for classification tasks.
It is designed to find the optimal hyperplane that separates different classes in the feature space.

1. kernel='linear' is the type of kernel function used to transform the input data into a higher-dimensional space.
The 'linear' kernel is used when the data is linearly separable
meaning that a straight line (or hyperplane in higher dimensions) can effectively separate the classes.

to check if your data is linearly separable or not you can use svm with linear kernel and plot the decision boundary using the function defined in svm1.py file.
or we can also use sns.scatterplot to visualize the data if it has only 2 features(in this case)

how to know which kernel to use when ur data is not linearly separable - 
You can try different kernels such as 'rbf' (Radial Basis Function) or 'poly' (Polynomial) and evaluate their performance using cross-validation.

2.C=1 is the regularization parameter that controls the trade-off between achieving a low training error and a low testing error (generalization).
A smaller C value creates a wider margin, allowing for more misclassifications but potentially improving generalization.
A larger C value creates a narrower margin, aiming to classify all training examples correctly but risking overfitting.
In this case, C=1.0 is a balanced choice.


'''
model=SVC(kernel='linear',C=1)
model.fit(X,y)
svm1.plot_svm_boundary(model,X,y)




