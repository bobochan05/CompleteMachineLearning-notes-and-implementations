'''
In real world , we always get imbalanced datasets and we have to build a model to predict the minority class 

WHY STUDY IMBALANCED DATA?
1.Because real-world data is almost never balanced. If you ignore this, your model can be confidently useless.
2.Think about common ML tasks:
Problem      	         Minority class
Fraud detection	         Fraud transactions (~0.1-1%)
Disease detection	     Sick patients
Spam detection	         Spam emails
Credit default	         Defaulters
Anomaly detection	     Faults / attacks

3.Accuracy becomes meaningless
Example:
99% non-fraud, 1% fraud, Model predicts “non-fraud” for everything
Accuracy = 99% 🎉
But fraud caught = 0 ❌
This is why imbalanced datasets force you to:
Question metrics and Understand what “good performance” really means

4.You learn the right evaluation metrics
With imbalance, you stop worshipping accuracy and start using:
Precision - How many predicted positives are correct?
Recall - How many actual positives did you catch?
F1-score - Precision-Recall tradeoff
ROC-AUC / PR-AUC
Confusion Matrix (your best friend)
👉 This is core ML maturity, not optional knowledge.

5.Model bias becomes visible
Most algorithms optimize overall loss, so they: Favor the majority class, Ignore rare but important events

Studying imbalance teaches you:
Why models are biased
How loss functions influence behavior
Why cost-sensitive learning matters

'''
#how to handle imbalanced data???
#METHOD 1 : UNDERSAMPLING

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
# Set random seed for reproducibility
np.random.seed(42)
# Generate imbalanced dataset
n_samples_1 = 25  # Number of samples in class 1
n_samples_2 = 375  # Number of samples in class 2
centers = [(0, 0), (2, 2)]  # Centers of each cluster
cluster_std = [1.5, 1.5]  # Standard deviation of each cluster

X, y = make_blobs(n_samples=[n_samples_1, n_samples_2],
                  centers=centers,
                  cluster_std=cluster_std,
                  random_state=0)

# Plotting
plt.figure(figsize=(8, 6))
plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color='red', label='Class 1')
plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color='blue', label='Class 2')
plt.title('2D Imbalanced Dataset with Two Classes')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.grid(True)
plt.show()

'''
imblearn is a library to handle imbalanced datasets -

'''
from imblearn.under_sampling import RandomUnderSampler

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42,stratify=y)
#creating an instance of the randomundersampler 
rus = RandomUnderSampler(random_state=42)
X_resampled, y_resampled = rus.fit_resample(X_train, y_train)
# Plotting
plt.figure(figsize=(8, 6))
plt.scatter(X_resampled[y_resampled == 0][:, 0], X_resampled[y_resampled == 0][:, 1], color='red', label='Class 1')
plt.scatter(X_resampled[y_resampled == 1][:, 0], X_resampled[y_resampled == 1][:, 1], color='blue', label='Class 2')
plt.title('2D Imbalanced Dataset with Two Classes')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.grid(True)
plt.show()

#training a model to see the recall score of class 0
from sklearn.svm import SVC
# Initialize and train RandomForest classifier on resampled data
model= SVC()
model.fit(X_resampled, y_resampled)

# Predict test set
y_pred = model.predict(X_test)
print(classification_report(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))

# Function to plot decision boundaries for resampled data
def plot_decision_boundaries_ros(X, y, model):
    plot_step = 0.02
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
                         np.arange(y_min, y_max, plot_step))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.3)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', s=20)
    plt.title("Decision Boundary (With Over Sampling)")
    plt.show()

# Plot decision boundary for resampled data
plot_decision_boundaries_ros(X, y, model)

'''
ADVANTAGES-
1.reduces bias 
2.faster training

DISADVANTGES-
1.information loss due to underfitting
2.sampling bias

'''





