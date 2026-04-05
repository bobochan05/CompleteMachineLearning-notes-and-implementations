'''
Random Forest - Classification 
THE DATA :
We will be using the same dataset through our discussions on classification with tree-methods (Decision Tree,Random Forests, and Gradient Boosted Trees) in order to compare performance metrics across these related models.

We will work with the "Palmer Penguins" dataset, as it is simple enough to help us fully understand how changing hyperparameters can change classification results.

Image
Data were collected and made available by Dr. Kristen Gorman and the Palmer Station, Antarctica LTER, a member of the Long Term Ecological Research Network.

Gorman KB, Williams TD, Fraser WR (2014) Ecological Sexual Dimorphism and Environmental Variability within a Community of Antarctic Penguins (Genus Pygoscelis). PLoS ONE 9(3): e90081. doi:10.1371/journal.pone.0090081

Summary: The data folder contains two CSV files. For intro courses/examples, you probably want to use the first one (penguins_size.csv).

penguins_size.csv: Simplified data from original penguin data sets. Contains variables:

species: penguin species (Chinstrap, Adélie, or Gentoo)
culmen_length_mm: culmen length (mm)
culmen_depth_mm: culmen depth (mm)
flipper_length_mm: flipper length (mm)
body_mass_g: body mass (g)
island: island name (Dream, Torgersen, or Biscoe) in the Palmer Archipelago (Antarctica)
sex: penguin sex
(Not used) penguins_lter.csv: Original combined data for 3 penguin species

Note: The culmen is "the upper ridge of a bird's beak"

Our goal is to create a model that can help predict a species of a penguin based on physical attributes,
then we can use that model to help researchers classify penguins in the field, instead of needing an experienced biologist
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df=pd.read_csv("C:\\Users\\soham\\Downloads\\penguins_size (1).csv")
df=df.dropna()
print(df.head())
X=pd.get_dummies(df.drop('species',axis=1) , drop_first=True)
y=df['species']

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.3, random_state=101)

from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier(n_estimators=100,max_features='sqrt',random_state=101)
model.fit(X_train,Y_train)

Y_preds=model.predict(X_test)
from sklearn.metrics import confusion_matrix,classification_report
cm=confusion_matrix(Y_preds,Y_test)
cr=classification_report(Y_preds,Y_test)
print("confusion matrix :\n",cm)
print("classification report :\n",cr)





