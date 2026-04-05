'''matrix plot'''

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
df = pd.read_csv(r"C:\Users\soham\Downloads\country_table.csv")
df = df.set_index('Countries')
print(df)

plt.figure(figsize=(10, 3))
sns.heatmap(data=df.drop('Life expectancy', axis=1),lw=1 , annot=True , cmap='viridis')

sns.clustermap(data=df.drop('Life expectancy', axis=1), col_cluster=False, cmap='viridis', standard_scale=1, figsize=(10, 5))

plt.show()
