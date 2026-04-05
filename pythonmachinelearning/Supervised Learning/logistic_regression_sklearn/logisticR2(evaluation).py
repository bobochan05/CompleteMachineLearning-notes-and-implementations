'''
coefficients interpretation:
Logistic regression coefficients are not interpreted like linear regression.They work in log-odds space

LINEAR REGRESSION MODEL : y = (b0*x0 + b1*x1 + b2*x2 + ... + bn*xn)
LOGISTIC REGRESSION MODEL : y = 1 / (1 + e^(-z)) , where z = (b0*x0 + b1*x1 + b2*x2 + ... + bn*xn)

The Logistic Regression model can be rearranged to : ln(y/(1-y)) = z = (b0*x0 + b1*x1 + b2*x2 + ... + bn*xn)
This means that for a one unit increase in feature xi, the log-odds of the outcome y increases by bi, holding all other features constant.
For example, if the coefficient for age is -0.05, it means that for each additional year of age, 
the log-odds of passing the hearing test decreases by 0.05, assuming physical_score remains constant.

'''
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
df=pd.read_csv("C:\\Users\\soham\\Downloads\\hearing_test (1).csv")
X=df[['age','physical_score']]
y=df['test_result']
import sklearn
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.1,random_state=101)
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)

'''
ROC curve:
The Receiver Operating Characteristic (ROC) curve is a graphical representation 
that illustrates the diagnostic ability of a binary classifier system as its discrimination threshold is varied.

Precision vs Recall curve:
The precision-recall curve is a graphical representation that illustrates 
the trade-off between precision and recall for a binary classifier system as its discrimination threshold is varied.
'''
#performance metrics 
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
acc=accuracy_score(y_test,y_pred)
print("Accuracy :",acc)

cm=(confusion_matrix(y_test,y_pred))
print("Confusion Matrix : \n",cm)
sns.heatmap(cm,annot=True)

cr=(classification_report(y_test,y_pred))
print("Classification Report : \n",cr)
'''
interpreting Classification Report:
                precision    recall  f1-score   support
    
             0       0.83      0.91      0.87        11
             1       0.75      0.60      0.67         5
    
      accuracy                           0.81        16
     macro avg       0.79      0.76      0.77        16
  weighted avg       0.81      0.81      0.81        16
  
Precision of class 0 : how many predicted 0 are actually 0 i.e TN/(TN+FN)
Precision of class 1 : how many predicted 1 are actually 1 i.e TP/(TP+FP)
Recall of class 0 :    how many actual 0 are predicted correctly i.e TN/(TN+FP)
Recall of class 1 :    how many actual 1 are predicted correctly i.e TP/(TP+FN)
Accuracy : (TP+TN)/(TP+TN+FP+FN)

'''
print( model.predict_proba(X_test))
#plotting ROC curve:
from sklearn.metrics import roc_curve, roc_auc_score
# Probabilities for positive class
y_prob = model.predict_proba(X_test)[:,1]
'''
[:,1] gives probabilities of positive class , y_prob[:,0] would give probabilities of negative class
y_prob = model.predict_proba(X_test) would give probabilities of both classes in a 2D array 
'''
# ROC values
fpr, tpr, thresholds = roc_curve(y_test, y_prob)

# AUC score
auc = roc_auc_score(y_test, y_prob)

# Plotting ROC curve
plt.figure()
plt.plot(fpr, tpr)
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")

plt.show()












