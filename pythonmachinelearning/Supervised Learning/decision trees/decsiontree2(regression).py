'''
decision trees can also be used for regression tasks.
It is used when the data is continous and cannot be classified into distinct classes.
1.Why use decision trees for regression?
Linear Regression cannot be used when data cannot separated by a straight line. 
Decision trees can capture non-linear relationships between features and the target variable.

2.If polynomial regression and SVR can model non-linearity, why do regression trees even exist?
Although Polynomial Regression, SVR, and Regression Trees can all model non-linear relationships, they do it in fundamentally different ways:

Model	                           How non-linearity is learned

Polynomial Regression	           By fitting a global equation
SVR	                               By learning a smooth function in high-dim space
Regression Tree                	   By learning if-else decision rules

'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


