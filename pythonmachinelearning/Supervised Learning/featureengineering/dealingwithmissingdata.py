import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
'''f=open("C:\\Users\\soham\\Downloads\\Ames_Housing_Feature_Description.txt",'r')
print(f.read())
reading the text file containing feature description of the dataset '''

df = pd.read_csv("C:\\Users\\soham\\Downloads\\Ames_outliers_removed.csv")
#print(df.head())
#print(df.info())
#print(df.isnull().sum())
#defining a function to calculate missing data percentage
def missing_percent(df):
    missing_data = df.isnull().sum()
    missing_percent = (missing_data / len(df))* 100
    missing_percent=missing_percent[missing_percent > 0].sort_values(ascending=False)   
    return missing_percent

#print(missing_percent(df))


'''
Removing Features or Removing Rows
If only a few rows relative to the size of your dataset are missing some values,
then it might just be a good idea to drop those rows. What does this cost you in terms of performace? 
It essentialy removes potential training/testing data, but if its only a few rows, its unlikely to change performance.

Sometimes it is a good idea to remove a feature entirely if it has too many null values. 
However, you should carefully consider why it has so many null values, in certain situations null could just be used as a separate category.

Take for example a feature column for the number of cars that can fit into a garage. Perhaps if there is no garage then there is a null value, instead of a zero. 
It probably makes more sense to quickly fill the null values in this case with a zero instead of a null. 
Only you can decide based off your domain expertise and knowledge of the data set!

'''

'''Let's explore how to choose to remove or fill in missing data for rows that are missing some data.
Let's choose some threshold where we decide it is ok to drop a row if its missing some data (instead of attempting to fill in that missing data point). 
We will choose 1% as our threshold. This means if less than 1% of the rows are missing this feature, we will consider just dropping that row, instead of dealing with the feature itself.
There is no right answer here, just use common sense and your domain knowledge of the dataset, obviously you don't want to drop a very high threshold like 50% ,
you should also explore correlation to the dataset, maybe it makes sense to drop the feature instead.

Based on the text description of the features, you will see that most of this missing data is actually NaN on purpose as a placeholder for 0 or "none".'''

#we will drop rows where more than 1% of the data is missing


print(df[df['Bsmt Full Bath'].isnull()])#It prints all rows of the DataFrame where the column Bsmt Full Bath has missing (NaN) values.
df=df.dropna(axis=0 , subset=['Total Bsmt SF'])
miss_percent = pd.Series(missing_percent(df))
print(miss_percent[miss_percent < 1])

print(df[df['Mas Vnr Area'].isnull()])#It prints all rows of the DataFrame where the column Mas Vnr Area has missing (NaN) values.
'''here we replace all the NaN values with 0 since missing value means no masonry veneer area'''
df=df['Mas Vnr Area'].fillna(0)

'''
Sometimes you may want to take the approach that above a certain missing percentage threshold, you will simply remove the feature from all the data.
For example if 99% of rows are missing a feature, it will not be predictive, since almost all the data does not have any value for it. 
In our particular data set, many of these high percentage NaN features are actually plasceholders for "none" or 0. 
But for the sake of showing variations on dealing with missing data, we will remove these features, instead of filling them in with the appropriate value.
'''
sns.barplot(x=miss_percent.index,y=miss_percent,hue=miss_percent)
# miss_percent.index gives the labels (feature names) for the x-axis
# miss_percent gives the corresponding missing percentages for the y-axis
plt.xticks(rotation=90)
plt.show()

'''
gar_str_cols = ['Garage Type', 'Garage Finish', 'Garage Qual', 'Garage Cond']
df[gar_str_cols] = df[gar_str_cols].fillna('None')
df['Garage Yr Blt'] = df['Garage Yr Blt'].fillna(0)

'''








